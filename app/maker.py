from bs4 import BeautifulSoup 
import os
import argparse
from string import Template

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

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, help='Input file')
parser.add_argument('--output', type=str, help='Output path')

input = parser.parse_args().input
output_dir = parser.parse_args().output

if input==None or not os.path.exists(input):
    print(f"File {input} not found")
    exit(-1)

# print input and output files
print(f"Input file: {input}")
print(f"Output path: {output_dir}")

# open file
with open(input, 'r') as f:
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

# get all simple components with kind Plant wich starts with 'GD'
simple_component_plant = bs_data.find_all('SimpleComponent', {'Kind':'PLANT'})
simple_component_plant = [x for x in simple_component_plant if x.get('Name').startswith('GD')]
simple_component_supervisor = simple_component_supervisor + simple_component_plant

supervisors = []
for supervisor in simple_component_supervisor:
    sup = {}
    sup['name'] = supervisor.get('Name')

    if(len(supervisor.find_all('NodeList')) > 1):
        print(f"Error: multiple NodeList on Supervisor {sup['name']}")
        exit(-1)
    state_list = []
    for node in supervisor.find_all('NodeList')[0].find_all('SimpleNode'):
        state_list.append({'Name':node.get('Name'), 'Initial': 1 if node.get('Initial')!=None else 0})
    sup['state_list'] = state_list
    
    edgeList = supervisor.find_all('EdgeList')[0].find_all('Edge')
    # if(len(EdgeList) > 1):
    #     print(f"Error: multiple EdgeList on Supervisor {sup['name']}")
    #     exit(-1)
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


# make file events.c
# Event btnON = {UNCONTROLLABLE, 0, "btnON", NULL};
events_c = ""

# make file events.h
# extern Event btnON;
events_h = ""

# create set callback list
# Events['Se'].set_callback(default_callback)
set_callback = ""

# create handle events list for test
# handle_event(Events['Se'])
handle_event = ""

i = 0
for event in event_list:
    event['Name'] = event['Name'].replace('.', '_')
    # Event on = {CONTROLLABLE, 0, "on", NULL};
    events_c += f"Event {event['Name']} = {{{event['Kind']}, {i}, SUP_DEBUG_STR(\"{event['Name']}\"), NULL}};\n"
    events_h += f"extern Event {event['Name']};\n"
    set_callback += f"  set_event_callback(&{event['Name']}, default_callback);\n"
    handle_event += f"  handle_event(&{event['Name']});\n"
    i = i + 1

fill_template(f"{base_dir}/template/src/supervisors/events-template.h",
                f"{output_dir}/src/supervisors/events.h", 
                {'events_h': events_h})

fill_template(f"{base_dir}/template/src/supervisors/events-template.c",
                f"{output_dir}/src/supervisors/events.c", 
                {'events_c': events_c})

fill_template(f"{base_dir}/template/src/main-template.c",
                f"{output_dir}/src/main.c", 
                {'set_callback': set_callback,
                'handle_event': handle_event})

#include "supervisors/sup.h"
# create include supervisor files
include_supervisors = ""

supervisor_initial_state = ""
supervisor_list_create = ""
supervisor_list_init = ""
supervisor_list_head = f"{supervisors[0]['name'].replace('.', '_')}_list"
handle_include_supervisors = ""
cmake_append_supervisors = ""

for sup_index in range(len(supervisors)):
    sup = supervisors[sup_index]
    sup['name'] = sup['name'].replace('.', '_')

    include_supervisors += f"#include \"supervisors/{sup['name']}.h\"\n"
    handle_include_supervisors += f"#include \"{sup['name']}.h\"\n"
    
    cmake_append_supervisors += f"list(APPEND SOURCE_FILES src/supervisors/{sup['name']}.c)\n"

    supervisor_list_create += f"extern SupervisorList {sup['name']}_list;\n"
    
    next_sup = f"&{supervisors[sup_index+1]['name']}_list" if sup_index < len(supervisors)-1 else "NULL"
    supervisor_list_init += f"SupervisorList {sup['name']}_list = {{&{sup['name']}, {next_sup}}};\n"
    
    # create event list
    # Alphabet sup_evt0;
    alphabet_create = ""

    # Alphabet sup_evt0 = {&on, &sup_evt1};
    alphabet_init = ""
    first_alphabet_event =f"{sup['name']}_{sup['event_list'][0]['Name']}_evt0"
    for i in range(len(sup['event_list'])):
        event = sup['event_list'][i]
        alphabet_create += f"Alphabet {sup['name']}_{event['Name']}_evt{i};\n"
        next_event_name = f"&{sup['name']}_{sup['event_list'][i+1]['Name']}_evt{i+1}" if i < len(sup['event_list'])-1  else 'NULL'
        alphabet_init += f"Alphabet {sup['name']}_{event['Name']}_evt{i} = {{&{event['Name']}, {next_event_name}}};\n"
        i=i+1

    # State sup_q0;
    state_create = ""

    # // State sup_q0 = {      true,       "q0", &sup_q0_t0};
    #          state_name      is_initial  name  first_transition
    state_initializer_dict = {} # filled in transition loop
    state_transition_create = {} # filled in transition loop
    state_transition_init = {} # filled in transition loop
    for state in sup['state_list']:
        # change . to _ in state name
        state_name = f"{sup['name']}_{state['Name'].replace('.', '_')}"
        state_create += f"State {state_name};\n"
        state_initializer_dict[state_name] = None
        state_transition_create[state_name] = []
        state_transition_init[state_name] = []

    j = 0
    for i in range(len(sup['transition_list'])):
        # get transition and next transition
        transition = sup['transition_list'][i]
        next_transition = sup['transition_list'][i+1] if i < len(sup['transition_list'])-1 else None
        
        # change . to _ in transition  Source name
        transition['Source'] = transition['Source'].replace('.', '_')
        if next_transition is not None:
            next_transition['Source'] = next_transition['Source'].replace('.', '_')
        # change . to _ in transition  Target name
        transition['Target'] = transition['Target'].replace('.', '_')
        if next_transition is not None:
            next_transition['Target'] = next_transition['Target'].replace('.', '_')
        # change . to _ in transition  Event name
        transition['Event'] = transition['Event'].replace('.', '_')
        if next_transition is not None:
            next_transition['Event'] = next_transition['Event'].replace('.', '_')

        # make source state name for transition
        state_name = f"{sup['name']}_{transition['Source']}"
        # if is first transition in state
        if(state_initializer_dict[state_name] is None):
            j = 0
        
        # make transition name
        transition_name = f"{sup['name']}_{transition['Source']}_t{j}"
        
        # fill state initializer if not filled in

        if(state_initializer_dict[state_name] is None):
            # find state to fill is_initial
            for state in sup['state_list']:
                state['Name'] = state['Name'].replace('.', '_')
                if state['Name'] == transition['Source']:
                    is_initial = 'false'
                    if state['Initial']==1:
                        is_initial = 'true'
                        supervisor_initial_state = f"{sup['name']}_{state['Name']}"
                    state_initializer_dict[state_name] = f"State {state_name} = {{{is_initial}, SUP_DEBUG_STR(\"{transition['Source']}\"), &{transition_name}}};\n"
                    break
        
        # make next transition name
        if next_transition is not None:
            if(state_initializer_dict[f"{sup['name']}_{next_transition['Source']}"] is None):
                next_name = 'NULL' #f"&{sup['name']}_{next_transition['Source']}_t{j}" if next_transition else 'NULL'
            else:
                next_name = f"&{sup['name']}_{next_transition['Source']}_t{j+1}" if next_transition else 'NULL'
        else:
            next_name = 'NULL'

        transition_create = f"Transition {transition_name};\n"
        transition_create_header = f"extern Transition {transition_name};\n"
        transition_init = f"Transition {transition_name} = {{&{transition['Event']}, &{sup['name']}_{transition['Target']}, {next_name}}};\n"
        state_transition_create[state_name].append(transition_create)
        state_transition_init[state_name].append(transition_init)
        
        # Create states         
        j = j + 1
        
    # Create transitions
    transitions_list = ""
    state_init = ""
    for state_name in state_initializer_dict:
        state_init += state_initializer_dict[state_name]
        transitions_list += "".join(state_transition_create[state_name])
        transitions_list += "".join(state_transition_init[state_name])
        transitions_list += "\n"

    # supervisor_create
    #  Supervisor sup = {&sup_q0, &sup_q0, NULL, &sup_evt0, "sup"};
    supervisor_create = f"Supervisor {sup['name']} = {{&{supervisor_initial_state}, &{supervisor_initial_state}, NULL,  &{first_alphabet_event}, \"{sup['name']}\"}};\n"
    # create supervisor file
    fill_template(f"{base_dir}/template/src/supervisors/supervisor-template.c",
                f"{output_dir}/src/supervisors/{sup['name']}.c",
                {'sup_name_source': sup['name'],
                'alphabet_create_source': alphabet_create,
                'alphabet_init_source':alphabet_init,
                'state_create_source': state_create,
                'state_init_source': state_init,
                'transitions_list_source': transitions_list,
                'supervisor_create_source': supervisor_create
                })

    fill_template(f"{base_dir}/template/src/supervisors/supervisor-template.h",
                f"{output_dir}/src/supervisors/{sup['name']}.h",
                {'supervisor_name_upper': sup['name'].upper(),
                'supervisor_create_header': f"extern Supervisor {sup['name']};\n"
                })

# -------- end of for "sup in supervisors:" ---------------

fill_template(f"{output_dir}/src/main.c",
                f"{output_dir}/src/main.c", 
                {'include_supervisors': include_supervisors})

fill_template(f"{base_dir}/template/src/supervisors/handle_event-template.c",
                f"{output_dir}/src/supervisors/handle_event.c", 
                {'supervisor_list_create': supervisor_list_create,
                'supervisor_list_init': supervisor_list_init,
                'supervisor_list_head': supervisor_list_head,
                'handle_include_supervisors':handle_include_supervisors})

fill_template(f"{base_dir}/template/CMakeLists-template.txt",
                f"{output_dir}/CMakeLists.txt", 
                {'cmake_append_supervisors': cmake_append_supervisors})

# print("Lista de eventos:")
# print(event_list)

# # print supervisor in readable format
# for sup in supervisors:
#     print(f"Supervisor {sup['name']}:")
#     print(f"\tEvents:")
#     for event in sup['event_list']:
#         print(f"\t\t{event['Name']}")
#     print(f"\tStates:")
#     for state in sup['state_list']:
#         print(f"\t\t{state['Name']}")
#     print(f"\tTransitions:")
#     for transition in sup['transition_list']:
#         print(f"\t\t{transition['Source']} -> {transition['Event']} -> {transition['Target']}")

