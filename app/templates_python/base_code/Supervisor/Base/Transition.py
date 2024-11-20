"""
Class for handling transitions
"""
from . import Event
from . import State

class Transition:
    """
    Class representing a transition between states triggered by an event.

    Attributes:
        event (Event): The event that triggers the transition.
        target (State): The target state of the transition.
    """

    def __init__(self, event: Event, target: State):
        """
        Initializes a new transition.

        Args:
            event (Event): The event that triggers the transition.
            target (State): The target state of the transition.

        Raises:
            TypeError: If 'event' is not an instance of Event or
            'target' is not an instance of State.
        """
        if not isinstance(event, Event):
            raise TypeError("event must be instance of Event")
        self.__event = event
        self.__target = target

    def get_event(self) -> Event:
        """
        Returns the event that triggers the transition.

        Returns:
            Event: The event that triggers the transition.
        """
        return self.__event

    def get_target(self) -> State:
        """
        Returns the target state of the transition.

        Returns:
            State: The target state of the transition.
        """
        return self.__target
