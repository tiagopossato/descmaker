"""
Arquivo principal do programa, responsável por ler o arquivo xml e gerar os arquivos python
Procura pelas tags SimpleComponent, com o atributo Kind="SUPERVISOR"
Já para os distuinguidores, procura pelas tags SimpleComponent, com o atributo Kind="PLANT" e Name="H*"
Cada supervisor ou distuinguidor é um arquivo python separado, com o nome do supervisor ou distuinguidor
"""
try:
    from bs4 import BeautifulSoup 
    import os
    import argparse
    from string import Template
    from utils import copy_directory, remove_directory
except ImportError as e:
    print("Import error: ", e)
    exit(-1)


# Specify the regex patterns to exclude files and directories
exclude_files = [
    r'\b\w*template\w*\b',  # Exclude a specific files with *template*
    r'\b\w*.pyc',  # Exclude a specific files with end with .pyc
    r'sup.py'  # Exclude a specific file
]

exclude_dirs = [
    r'__pycache__'  # Exclude directories like 'internal1', 'internal2', etc.
]


class CustomTemplate(Template):
	delimiter = '%$%'

def fill_template(template, dest, template_dict):
    # verify if script is being executed on Windows and convert paths to Windows format
    if os.name == 'nt':
        template = template.replace('/', '\\')
        dest = dest.replace('/', '\\')

    # make the names of the files
    with open(template, 'r') as f:
        src = CustomTemplate(f.read())
        result = src.safe_substitute(template_dict)

    arquivo = open(dest,'w')
    arquivo.write(result)
    arquivo.close()

base_dir = os.path.dirname(os.path.realpath(__file__))


def convert_supervisor(input_file, output_dir):
    
    if input_file==None or not os.path.exists(input_file):
        print(f"File {input_file} not found")
        # raise exception
        raise FileNotFoundError

    # join script path with 'base_code' folder
    base_code_path = os.path.join(base_dir, 'base_code')

    # Call the function to copy the directory structure
    try:
        copy_directory(base_code_path, output_dir, exclude_files, exclude_dirs)
        print("Directory copied successfully!")
    except Exception as e:
        print("Directory copy failed!")
        exit(-1)
        
    # print input and output files
    print(f"Input file: {input_file}")
    print(f"Output path: {output_dir}")

    # open file
    with open(input_file, 'r') as f:
        data = f.read() 

    # parse file with BeautifulSoup
    bs_data = BeautifulSoup(data, "xml")

    # get all Events
    event_decl_list = bs_data.find_all('EventDeclList')
    event_list = []
    for e in event_decl_list[0].find_all('EventDecl'):
        if(e.get('Kind') == 'PROPOSITION'):
            continue
        event_list.append({'Kind':e.get('Kind'), 'Name':e.get('Name')})


    # get all supervisors
    simple_component_supervisor = bs_data.find_all('SimpleComponent', {'Kind':'SUPERVISOR'})

    # get all simple components with kind Plant wich starts with 'H'
    simple_component_plant = bs_data.find_all('SimpleComponent', {'Kind':'PLANT'})
    simple_component_plant = [x for x in simple_component_plant if x.get('Name').startswith('H')]
    simple_component_supervisor = simple_component_supervisor + simple_component_plant

    supervisors = []
    # create supervisor list for use in trigger_event
    supervisor_list = ""

    distinguishers = []
    # create supervisor list for use in trigger_event
    distinguisher_list = ""
    
    for supervisor in simple_component_supervisor:
        sup = {}
        sup['name'] = supervisor.get('Name')

        if(len(supervisor.find_all('NodeList')) > 1):
            print(f"Error: multiple NodeList on Supervisor {sup['name']}")
            # raise exception
            raise Exception
        state_list = []
        for node in supervisor.find_all('NodeList')[0].find_all('SimpleNode'):
            state_list.append({'Name':node.get('Name'), 'Initial': 1 if node.get('Initial')!=None else 0})
        sup['state_list'] = state_list

        edgeList = supervisor.find_all('EdgeList')[0].find_all('Edge')
        # order edgeList by Source
        edgeList = sorted(edgeList, key=lambda k: k.get('Source'))

        transition_list = []
        local_event_list = []
        for node in edgeList:
            for evt in node.find_all('SimpleIdentifier'):
                transition_list.append({'Source':node.get('Source'), 'Event':evt.get('Name'), 'Target':node.get('Target')})
                for x in event_list:
                    if x['Name'] == evt.get('Name'):
                        e = {'Kind':x['Kind'], 'Name':evt.get('Name')}
                        if(e not in local_event_list):
                            local_event_list.append(e)
                        break
        sup['transition_list'] = transition_list
        sup['event_list'] = local_event_list
        supervisors.append(sup)

        if supervisor.get('Kind') == 'SUPERVISOR':
            supervisor_list += f"{sup['name']},"
        if supervisor.get('Kind') == 'PLANT':
            distinguisher_list += f"{sup['name']},"


    # make file events_names.py
    # 'Se': Event(EventKind.UNCONTROLLABLE, 0, "Se"),
    events = ""

    # create set action list
    # Events['Se'].set_action(default_action)
    set_action = ""

    # create handle events list for test
    # trigger_event(Events['Se'])
    trigger_event = ""

    i = 0
    for event in event_list:
        event['Name'] = event['Name'].replace('.', '_')
        events += f"    '{event['Name']}': Event(EventKind.{event['Kind']}, {i}, '{event['Name']}'),\n"
        if event['Kind'] == 'CONTROLLABLE':
            set_action += f"Events['{event['Name']}'].set_action(default_action)\n"
        if event['Kind'] == 'UNCONTROLLABLE':
            trigger_event += f"    trigger_event(Events['{event['Name']}'])\n"
        i = i + 1

    fill_template(f"{base_dir}/template/Supervisor/events-template.py",
                    f"{output_dir}/Supervisor/events.py", 
                    {'events': events})

    fill_template(f"{base_dir}/template/main-template.py",
                    f"{output_dir}/main.py", 
                    {'set_action': set_action,
                    'trigger_event': trigger_event})

    # create import list
    import_list = ""

    for sup in supervisors:
        import_list += f"from .{sup['name']} import {sup['name']}\n"
        # supervisor_list += f"{sup['name']},"
        # Create states
        # q0_state = State("q0", True)
        states = ""
        for state in sup['state_list']:
            # change . to _ in state name
            state['Name'] = state['Name'].replace('.', '_')
            states += f"{state['Name']}_state = State(\"{state['Name']}\", {True if state['Initial']==1 else False})\n"

        # Create transitions
        # q0_state.add_transition(Events['btnON'], q3_state)
        transitions = ""
        for transition in sup['transition_list']:
            # change . to _ in transition  Source name
            transition['Source'] = transition['Source'].replace('.', '_')
            # change . to _ in transition  Target name
            transition['Target'] = transition['Target'].replace('.', '_')
            transitions += f"{transition['Source']}_state.add_transition(Events['{transition['Event']}'], {transition['Target']}_state)\n"

        # create event list
        # event_list.append(btnON_evt)
        alphabet = ""
        for event in sup['event_list']:
            alphabet += f"alphabet.append(Events['{event['Name']}'])\n"

        # create state list
        # state_list.append(q0_state)
        state_list = ""
        for state in sup['state_list']:
            state_list += f"state_list.append({state['Name']}_state)\n"

        # create supervisor file
        fill_template(f"{base_dir}/template/Supervisor/supervisors/supervisor-template.py",
                    f"{output_dir}/Supervisor/supervisors/{sup['name']}.py",
                    {'events': events,
                    'states': states,
                    'transitions': transitions,
                    'alphabet': alphabet,
                    'state_list': state_list,
                    'supervisor_name': sup['name']})

    fill_template(f"{base_dir}/template/Supervisor/supervisors/__init__-template.py",
                    f"{output_dir}/Supervisor/supervisors/__init__.py", 
                    {'import_list': import_list})

    # remove last comma
    if len(distinguisher_list) == 0:
        supervisor_list = supervisor_list[:-1]
    
    distinguisher_list = distinguisher_list[:-1]
    
    fill_template(f"{base_dir}/template/Supervisor/__init__-template.py",
                    f"{output_dir}/Supervisor/__init__.py", 
                    {'supervisor_list': supervisor_list,
                     'distinguisher_list': distinguisher_list})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, help='Input file', required=True)
    parser.add_argument('--output', type=str, help='Output path', default='generated_code', required=False)

    input_file = parser.parse_args().input
    output_dir = parser.parse_args().output

    try:
        convert_supervisor(input_file, output_dir)
        print("Supervisor converted successfully!")
    except Exception as e:
        # remove output directory
        remove_directory(output_dir)
        print(e)
