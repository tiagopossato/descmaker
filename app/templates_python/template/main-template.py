"""
Main controller
"""
from Supervisor import Events, Event, trigger_event, controller_start

def default_action(event: Event):
    """
    Default action for example
    """
    print(f"Default action for event {event.get_name()}")

if __name__ == '__main__':
    # set default action for example
%$%{set_action}
    # start the controller
    controller_start()

    # handle events for test
%$%{trigger_event}