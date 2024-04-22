"""
Events from supremica file
"""
from . import Event, EventKind

# Create events
Events = {
%$%{events}}

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