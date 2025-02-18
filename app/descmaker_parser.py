"""
Parser
"""
import sys

try:
    from bs4 import BeautifulSoup
    from utils import validate_and_update_variable_name
except ImportError as e:
    print("Import error: ", e)
    sys.exit(-1)

def descmaker_parser(input_file):
    """
    parser
    """
    # open file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.read()

    # parse file with BeautifulSoup
    bs_data = BeautifulSoup(data, "xml")

    # get all Events
    event_decl_list = bs_data.find_all('EventDeclList')
    global_event_list = []
    for e in event_decl_list[0].find_all('EventDecl'):
        if e.get('Kind') == 'PROPOSITION':
            continue
        global_event_list.append({'Kind':e.get('Kind'), 'Name':e.get('Name')})

    # get all supervisors
    simple_component_supervisor = bs_data.find_all('SimpleComponent', {'Kind':'SUPERVISOR'})

    supervisors = []

    # create supervisor list for use in trigger_event
    supervisor_list = ""

    for supervisor in simple_component_supervisor:
        sup = {}
        sup['name'] = validate_and_update_variable_name(supervisor.get('Name'))

        if len(supervisor.find_all('NodeList')) > 1:
            print(f"Error: multiple NodeList on Supervisor {sup['name']}")
            sys.exit(-1)
        state_list = []
        #Create a list of states
        for node in supervisor.find_all('NodeList')[0].find_all('SimpleNode'):
            state_list.append({'Name':node.get('Name'),
                               'Initial': 1 if node.get('Initial') is not None else 0})
        sup['state_list'] = state_list

        # Create the list of edges
        edge_list = supervisor.find_all('EdgeList')[0].find_all('Edge')
        # order edgeList by Source
        edge_list = sorted(edge_list, key=lambda k: k.get('Source'))

        transition_list = []
        local_event_list = []
        # Every edge has a source and a target
        for transition in edge_list:
            for evt in transition.find_all('SimpleIdentifier'):
                # ignore guards
                if evt.get('Name').startswith("{"):
                    continue
                # make the transition list
                transition_list.append({'Source':transition.get('Source'),
                                        'Event':evt.get('Name'), 'Target':transition.get('Target')})
                # create a local event list
                for global_event in global_event_list:
                    if global_event['Name'] == evt.get('Name'):
                        local_event = {'Kind':global_event['Kind'], 'Name':evt.get('Name')}
                        if local_event not in local_event_list:
                            local_event_list.append(local_event)
                        break
        sup['transition_list'] = transition_list
        sup['event_list'] = local_event_list

        supervisors.append(sup)

        # used only for python output
        if supervisor.get('Kind') == 'SUPERVISOR':
            supervisor_list += f"{sup['name']},"

    # remove last comma. Used only for python output
    supervisor_list = supervisor_list[:-1]

    return supervisors, global_event_list, supervisor_list
