"""
Class for handling events
"""
# pylint: disable=C0103

from enum import Enum

class EventKind(Enum):
    """
    Enumeration to define event types.

    Attributes:
        CONTROLLABLE (int): Controllable event.
        UNCONTROLLABLE (int): Uncontrollable event.
    """
    CONTROLLABLE = 0
    UNCONTROLLABLE = 1

class Event:
    """
    Class representing an event.

    Attributes:
        kind (EventKind): The type of the event.
        event_id (int): The unique identifier of the event.
        name (str): The name of the event.
        action (callable, optional): The action associated with the event.
    """

    def __init__(self, kind: EventKind, event_id: int, name: str):
        """
        Initializes a new event.

        Args:
            kind (EventKind): The type of the event.
            event_id (int): The unique identifier of the event.
            name (str): The name of the event.

        Raises:
            TypeError: If 'kind' is not an instance of EventKind or 'event_id' is not an integer.
        """
        if not isinstance(kind, EventKind):
            raise TypeError("kind must be instance of EventKind")
        if not isinstance(event_id, int):
            raise TypeError("event_id must be an integer")

        self.__kind = kind
        self.__event_id = event_id
        self.__name = name
        self.__action = None

    def get_kind(self) -> EventKind:
        """
        Returns the type of the event.

        Returns:
            EventKind: The type of the event.
        """
        return self.__kind

    def is_controllable(self) -> bool:
        """
        Checks if the event is controllable.

        Returns:
            bool: True if the event is controllable, False otherwise.
        """
        return self.__kind == EventKind.CONTROLLABLE

    def get_name(self) -> str:
        """
        Returns the name of the event.

        Returns:
            str: The name of the event.
        """
        return self.__name

    def get_id(self) -> int:
        """
        Returns the unique identifier of the event.

        Returns:
            int: The unique identifier of the event.
        """
        return self.__event_id

    def set_action(self, action):
        """
        Sets the action associated with the event.

        Args:
            action (callable): The action to be associated with the event.
        """
        self.__action = action

    def run_action(self):
        """
        Executes the action associated with the event, if any.
        """
        if self.__action is not None:
            self.__action(self)
