from Supervisor import Events, Event, trigger_event

def default_action(event: Event):
    """
    Default action for example
    """
    print(f"Default action for event {event.get_name()}")

# set default action for example
Events['a1'].set_action(default_action)
Events['a2'].set_action(default_action)
Events['a0'].set_action(default_action)
Events['a3'].set_action(default_action)
Events['a4'].set_action(default_action)
Events['a5'].set_action(default_action)


if __name__ == '__main__':
    # handle events for teste
    trigger_event(Events['b1'])
    trigger_event(Events['b2'])
    trigger_event(Events['se'])
    trigger_event(Events['b0'])
    trigger_event(Events['b3'])
    trigger_event(Events['b4'])
    trigger_event(Events['b5'])

