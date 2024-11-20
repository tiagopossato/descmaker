"""
Verifies that the event is enabled, runs the event and its action
"""
from threading import Lock
from . import Event, Events
from . import EventKind
from . import supervisors_list
from . import log_state


# create a lock
lock = Lock()

def handle_event(event: Event):
    """
    Handles the given event by verifying its type and checking if 
    it is enabled for execution by any supervisor.

    Args:
        event (Event): The event to be handled.

    Raises:
        TypeError: If the provided event is not an instance of Event.

    Returns:
        bool: True if the event is successfully handled and executed by 
        at least one supervisor, False otherwise.
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
    """
    Retrieves a list of controllable events.

    This function filters through all events and returns those that are of the kind 'CONTROLLABLE'.

    Returns:
        list: A list of controllable events.
    """
    return [event for event in Events.values() if event.get_kind() == EventKind.CONTROLLABLE]


def trigger_event(event: Event):
    """
    Triggers the given event. If the event cannot be handled, it returns False.
    Otherwise, it runs the event's action and recursively triggers any controllable events.

    Args:
        event (Event): The event to be triggered.

    Returns:
        bool: True if the event and any subsequent controllable events are successfully triggered, 
        False otherwise.
    """
    if not handle_event(event):
        return False

    event.run_action()
    for _event in get_controllable_events():
        # print(f"Automatic running event: {event.get_name()}")
        if trigger_event(_event):
            break
    return True
