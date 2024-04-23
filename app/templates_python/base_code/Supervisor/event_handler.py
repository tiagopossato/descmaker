"""
Verifies that the event is enabled, runs the event and its action
"""
from . import Event, Events
from . import EventKind
from . import supervisors_list, distinguishers_list
from . import log_error, log_state
from threading import Lock

# create a lock
lock = Lock()

def handle_event(event: Event):
    """
    Handle event
    """    
    if not isinstance(event, Event):
        raise TypeError("event must be instance of Event")
    #print(f"\n-----------------------------------------\nRunning event: {event.get_name()}")
    with lock:
        # print(f"Event: {event.get_name()}")
        execution_list = []
        for sup in supervisors_list:
            # verify if event is in Alphabet of supervisor
            # if not, ignore because the supervisor does not observe the event
            if event in sup.get_alphabet():
                # verify if event is enabled
                if event in sup.get_enabled_events():
                    # if enabled, add to execution list
                    execution_list.append(sup)
                else:
                    # log_error(event, sup, f"Event not enabled")
                    return False
        # same from distinguishers
        for dis in distinguishers_list:
            if event in dis.get_alphabet():
                if event in dis.get_enabled_events():
                    execution_list.append(dis)
                else:
                    return False
                
        # verify len of execution_list
        # if len is 0, no supervisor is observing the event
        if len(execution_list) == 0:
            print(f"Event {event.get_name()} not enabled")
            return False
        
        # run event
        for sup in execution_list:
            sup.run(event)
            log_state(event, [sup])
    return True


def get_controllable_events():
    return [event for event in Events.values() if event.get_kind() == EventKind.CONTROLLABLE]


def trigger_event(event: Event):
    if(not handle_event(event)):
        return False
    
    event.run_action()
    for event in get_controllable_events():
        # print(f"Automatic running event: {event.get_name()}")
        if trigger_event(event):
            break
    return True
