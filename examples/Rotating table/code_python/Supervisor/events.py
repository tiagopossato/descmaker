"""
Events from supremica file
"""
from . import Event, EventKind

# Create events
Events = {
    'a1': Event(EventKind.CONTROLLABLE, 0, 'a1'),
    'b1': Event(EventKind.UNCONTROLLABLE, 1, 'b1'),
    'a2': Event(EventKind.CONTROLLABLE, 2, 'a2'),
    'b2': Event(EventKind.UNCONTROLLABLE, 3, 'b2'),
    'se': Event(EventKind.UNCONTROLLABLE, 4, 'se'),
    'a0': Event(EventKind.CONTROLLABLE, 5, 'a0'),
    'b0': Event(EventKind.UNCONTROLLABLE, 6, 'b0'),
    'a3': Event(EventKind.CONTROLLABLE, 7, 'a3'),
    'a4': Event(EventKind.CONTROLLABLE, 8, 'a4'),
    'b3': Event(EventKind.UNCONTROLLABLE, 9, 'b3'),
    'b4': Event(EventKind.UNCONTROLLABLE, 10, 'b4'),
    'a5': Event(EventKind.CONTROLLABLE, 11, 'a5'),
    'b5': Event(EventKind.UNCONTROLLABLE, 12, 'b5'),
}

def get_event_by_id(event_id: int) -> Event:
    """
    Get event by id
    """
    if not isinstance(event_id, int):
        raise TypeError("event_id must be an integer")

    for event in Events.values():
        if event.get_id() == event_id:
            return event
    return None