"""
Class for handling states
"""
from typing import List

from .Event import Event
from .Transition import Transition

class State:
    """
    Class representing a state.

    Attributes:
        name (str): The name of the state.
        is_start (bool): Indicates if this state is the start state.
        transitions (list): List of transitions from this state.
    """

    def __init__(self, name: str, is_start: bool = False):
        """
        Initializes a new state.

        Args:
            name (str): The name of the state.
            is_start (bool, optional): Indicates if this state is the start state. 
            Defaults to False.

        Raises:
            TypeError: If 'is_start' is not a boolean.
        """
        if not isinstance(is_start, bool):
            raise TypeError("is_start must be a boolean")
        self.__is_start = is_start
        self.__name = name
        self.__transitions = []

    def add_transition(self, event: Event, target: "State"):
        """
        Adds a new transition to the transitions list if it doesn't already exist.
        If the transition already exists, prints a message indicating that.
        The transition is created using the Transition class with the event 
        and target state as parameters.

        This method is only executed at the start of the application, 
        thus it doesn't impact overall performance.

        Args:
            event (Event): The event triggering the transition.
            target (State): The target state of the transition.

        Raises:
            TypeError: If 'event' is not an instance of Event or 'target' is not an 
            instance of State.
        """
        if not isinstance(event, Event):
            raise TypeError("event must be instance of Event")
        if not isinstance(target, type(self)):
            raise TypeError("target must be instance of State")

        if self.get_transition(event, target) is None:
            self.__transitions.append(Transition(event, target))
        else:
            print(f"Transition from state {self.get_name()} to state {target.get_name()} "
                  f"with the event {event.get_name()} already exists.")

    def get_transition(self, event: Event, target: "State"):
        """
        Searches the transitions list for a transition with the specified event and target state.
        If found, returns the transition. Otherwise, returns None.

        Args:
            event (Event): The event triggering the transition.
            target (State): The target state of the transition.

        Raises:
            TypeError: If 'event' is not an instance of Event.

        Returns:
            Transition or None: The found transition or None if not found.
        """
        if not isinstance(event, Event):
            raise TypeError("event must be instance of Event")
        for transition in self.__transitions:
            if transition.get_event() == event and transition.get_target() == target:
                return transition
        return None

    def get_transitions(self) -> List[Transition]:
        """
        Returns the list of transitions from this state.

        Returns:
            list: List of transitions.
        """
        return self.__transitions

    def get_enabled_events(self) -> List[Event]:
        """
        Returns the list of events that are enabled from this state.

        Returns:
            list: List of enabled events.
        """
        return [tr.get_event() for tr in self.__transitions]

    def get_enabled_controllable_events(self) -> List[Event]:
        """
        Returns the list of controllable events that are enabled from this state.

        Returns:
            list: List of enabled controllable events.
        """
        return [tr.get_event() for tr in self.__transitions if tr.get_event().is_controllable()]

    def get_name(self) -> str:
        """
        Returns the name of the state.

        Returns:
            str: The name of the state.
        """
        return self.__name

    def is_start(self) -> bool:
        """
        Checks if this state is the start state.

        Returns:
            bool: True if this is the start state, False otherwise.
        """
        return self.__is_start
