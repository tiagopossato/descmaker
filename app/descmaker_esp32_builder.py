from utils import fill_template

def descmaker_esp32_builder(supervisors, global_event_list, base_dir, output_dir):

    # make file events.c
    # Event btnON = {UNCONTROLLABLE, 0, "btnON", NULL};
    events_c = ""
    controllable_event_list = ""

    # make file events.h
    # extern Event btnON;
    events_h = ""

    # create set action list
    # Events['Se'].set_action(default_action)
    set_action = ""

    # create handle events list for test
    # trigger_event(Events['Se'])
    trigger_event = ""

    i = 0
    for event in global_event_list:
        event['Name'] = event['Name'].replace('.', '_')
        # Event on = {CONTROLLABLE, 0, "on", NULL};
        events_c += f"Event {event['Name']} = {{{event['Kind']}, {i}, SUP_DEBUG_STR(\"{event['Name']}\"), NULL}};\n"
        events_h += f"extern Event {event['Name']};\n"
        # set examples
        if event['Kind'] == 'CONTROLLABLE':
            set_action += f"  set_event_action(&{event['Name']}, default_action);\n"
            controllable_event_list += f"&{event['Name']},"
        if event['Kind'] == 'UNCONTROLLABLE':
            trigger_event += f"  trigger_event(&{event['Name']});\n" 
        i = i + 1

    # remove last comma on controllable_event_list
    controllable_event_list = controllable_event_list[:-1]

    # count controllable events
    events_controllable_count = len([x for x in global_event_list if x['Kind'] == 'CONTROLLABLE'])
    
    fill_template(f"{base_dir}/templates_esp-idf/template/components/event_handler/events-template.h",
                    f"{output_dir}/components/event_handler/events.h", 
                    {'events_controllable_count': events_controllable_count,
                    'events_h': events_h})

    fill_template(f"{base_dir}/templates_esp-idf/template/components/event_handler/events-template.c",
                    f"{output_dir}/components/event_handler/events.c", 
                    {'events_c': events_c,
                     'controllable_event_list':controllable_event_list})

    fill_template(f"{base_dir}/templates_esp-idf/template/main/main-template.c",
                    f"{output_dir}/main/main.c", 
                    {'set_action': set_action,
                    'trigger_event': trigger_event})

    #include "supervisors/sup.h"
    # create include supervisor files
    # include_supervisors = ""

    supervisor_initial_state = ""
    supervisor_list_create = ""
    supervisor_list_init = ""
    supervisor_list_head = f"{supervisors[0]['name'].replace('.', '_')}_list"
    handle_include_supervisors = ""
    cmake_append_supervisors = ""
    index = 0
    for sup_index in range(len(supervisors)):
        sup = supervisors[sup_index]
        # DONE: Comentado pois a função check_and_update remove os pontos e mais
        # sup['name'] = sup['name'].replace('.', '_')

        # include_supervisors += f"#include \"supervisors/{sup['name']}.h\"\n"
        handle_include_supervisors += f"#include \"{sup['name']}.h\"\n"
        
        cmake_append_supervisors += f"                    \"{sup['name']}.c\"\n"

        supervisor_list_create += f"extern SupervisorList {sup['name']}_list;\n"
        
        next_sup = f"&{supervisors[sup_index+1]['name']}_list" if sup_index < len(supervisors)-1 else "NULL"
        if(index == 0):
            supervisor_list_init += f"SupervisorList sup_list = {{&{sup['name']}, {next_sup}}};\n"
        else:
            supervisor_list_init += f"SupervisorList {sup['name']}_list = {{&{sup['name']}, {next_sup}}};\n"
        
        # create event list
        # Alphabet sup_evt0;
        alphabet_create = ""

        # Alphabet sup_evt0 = {&on, &sup_evt1};
        alphabet_init = ""
        first_alphabet_event =f"{sup['name']}_{sup['event_list'][0]['Name']}_evt0"
        for i in range(len(sup['event_list'])):
            event = sup['event_list'][i]
            alphabet_create += f"const Alphabet {sup['name']}_{event['Name']}_evt{i};\n"
            next_event_name = f"&{sup['name']}_{sup['event_list'][i+1]['Name']}_evt{i+1}" if i < len(sup['event_list'])-1  else 'NULL'
            alphabet_init += f"const Alphabet {sup['name']}_{event['Name']}_evt{i} = {{&{event['Name']}, {next_event_name}}};\n"
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
            state_create += f"const State {state_name};\n"
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
                        state_initializer_dict[state_name] = f"const State {state_name} = {{{is_initial}, SUP_DEBUG_STR(\"{transition['Source']}\"), &{transition_name}}};\n"
                        break
            
            # make next transition name
            if next_transition is not None:
                if(state_initializer_dict[f"{sup['name']}_{next_transition['Source']}"] is None):
                    next_name = 'NULL' #f"&{sup['name']}_{next_transition['Source']}_t{j}" if next_transition else 'NULL'
                else:
                    next_name = f"&{sup['name']}_{next_transition['Source']}_t{j+1}" if next_transition else 'NULL'
            else:
                next_name = 'NULL'

            transition_create = f"const Transition {transition_name};\n"
            # transition_create_header = f"extern Transition {transition_name};\n"
            transition_init = f"const Transition {transition_name} = {{&{transition['Event']}, &{sup['name']}_{transition['Target']}, {next_name}}};\n"
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
        fill_template(f"{base_dir}/templates_esp-idf/template/components/supervisors/supervisor-template.c",
                    f"{output_dir}/components/supervisors/{sup['name']}.c",
                    {'sup_name_source': sup['name'],
                    'alphabet_create_source': alphabet_create,
                    'alphabet_init_source':alphabet_init,
                    'state_create_source': state_create,
                    'state_init_source': state_init,
                    'transitions_list_source': transitions_list,
                    'supervisor_create_source': supervisor_create
                    })

        fill_template(f"{base_dir}/templates_esp-idf/template/components/supervisors/supervisor-template.h",
                    f"{output_dir}/components/supervisors/{sup['name']}.h",
                    {'supervisor_name_upper': sup['name'].upper(),
                    'supervisor_create_header': f"extern Supervisor {sup['name']};\n"
                    })
        index += 1

    # -------- end of for "sup in supervisors:" ---------------

    fill_template(f"{base_dir}/templates_esp-idf/template/components/supervisors/supervisor_list-template.c",
                    f"{output_dir}/components/supervisors/supervisor_list.c", 
                    {'supervisor_list_create': supervisor_list_create,
                    'supervisor_list_init': supervisor_list_init,
                    'supervisor_list_head': supervisor_list_head,
                    'handle_include_supervisors':handle_include_supervisors})

    fill_template(f"{base_dir}/templates_esp-idf/template/components/supervisors/CMakeLists-template.txt",
                    f"{output_dir}/components/supervisors/CMakeLists.txt", 
                    {'cmake_append_supervisors': cmake_append_supervisors})
