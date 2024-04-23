from utils import fill_template

def descmaker_python_builder(supervisors, global_event_list, supervisor_list, distinguisher_list, base_dir, output_dir):
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
    for event in global_event_list:
        event['Name'] = event['Name'].replace('.', '_')
        events += f"    '{event['Name']}': Event(EventKind.{event['Kind']}, {i}, '{event['Name']}'),\n"
        if event['Kind'] == 'CONTROLLABLE':
            set_action += f"Events['{event['Name']}'].set_action(default_action)\n"
        if event['Kind'] == 'UNCONTROLLABLE':
            trigger_event += f"    trigger_event(Events['{event['Name']}'])\n"
        i = i + 1

    fill_template(f"{base_dir}/templates_python/template/Supervisor/events-template.py",
                    f"{output_dir}/Supervisor/events.py", 
                    {'events': events})

    fill_template(f"{base_dir}/templates_python/template/main-template.py",
                    f"{output_dir}/main.py", 
                    {'set_action': set_action,
                    'trigger_event': trigger_event})

    # create import list
    import_list = ""

    for sup in supervisors:
        import_list += f"from .{sup['name']} import {sup['name']}\n"
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
        fill_template(f"{base_dir}/templates_python/template/Supervisor/supervisors/supervisor-template.py",
                    f"{output_dir}/Supervisor/supervisors/{sup['name']}.py",
                    {'events': events,
                    'states': states,
                    'transitions': transitions,
                    'alphabet': alphabet,
                    'state_list': state_list,
                    'supervisor_name': sup['name']})

    fill_template(f"{base_dir}/templates_python/template/Supervisor/supervisors/__init__-template.py",
                    f"{output_dir}/Supervisor/supervisors/__init__.py", 
                    {'import_list': import_list})
    
    fill_template(f"{base_dir}/templates_python/template/Supervisor/__init__-template.py",
                    f"{output_dir}/Supervisor/__init__.py", 
                    {'supervisor_list': supervisor_list,
                     'distinguisher_list': distinguisher_list})