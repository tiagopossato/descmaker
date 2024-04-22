"""
Eventos lidos no arquivo do supremica
"""
from . import Event, EventKind

# Create events
Events = {
    'btn': Event(EventKind.UNCONTROLLABLE, 0, 'btn'),
    'liga': Event(EventKind.CONTROLLABLE, 1, 'liga'),
    'desliga': Event(EventKind.CONTROLLABLE, 2, 'desliga'),
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