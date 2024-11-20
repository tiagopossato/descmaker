"""
Class for handling the supervisor
"""
from typing import List
from . import State
from . import Event

class Supervisor:
    """
    Class representing a supervisor.

    Attributes:
        _name (str): The name of the supervisor.
        _states_list (List[State]): The list of states managed by the supervisor.
        _alphabet (List[Event]): The list of events that the supervisor can handle.
    """

    def __init__(self, _name: str, _states_list: List[State], _alphabet: List[Event]):
        """
        Initializes a new supervisor.

        Args:
            _name (str): The name of the supervisor.
            _states_list (List[State]): The list of states managed by the supervisor.
            _alphabet (List[Event]): The list of events that the supervisor can handle.

        Raises:
            TypeError: If '_states_list' is not a list of State instances or 
            '_alphabet' is not a list of Event instances.
            Exception: If there is not exactly one start state in '_states_list'.
        """
        if not all(isinstance(x, State) for x in _states_list):
            raise TypeError("_states_list must be List[State]")

        if not all(isinstance(x, Event) for x in _alphabet):
            raise TypeError("_alphabet must be List[Event]")

        self.__name = _name
        self.__alphabet = _alphabet
        # Verify if the states list has only one start state
        start_states = [state for state in _states_list if state.is_start()]
        if len(start_states) != 1:
            raise Exception("The states list must have only one start state.")

        self.__start = start_states[0]
        self.__current_state = self.__start
        self.__last_state = self.__start
        print(f"Starting supervisor {self.__name}. Start state: {self.__start.get_name()}")

    def get_start_state(self):
        """
        Returns the start state of the supervisor.

        Returns:
            State: The start state.
        """
        return self.__start

    def get_current_state(self) -> State:
        """
        Returns the current state of the supervisor.

        Returns:
            State: The current state.
        """
        return self.__current_state

    def get_last_state(self) -> State:
        """
        Returns the last state of the supervisor.

        Returns:
            State: The last state.
        """
        return self.__last_state

    def run(self, evt: Event) -> bool:
        """
        Runs the supervisor with the given event.

        Args:
            evt (Event): The event to be processed.

        Raises:
            TypeError: If 'evt' is not an instance of Event.

        Returns:
            bool: True if the event is processed successfully, False otherwise.
        """
        if not isinstance(evt, Event):
            raise TypeError("evt must be an Event")
        # print(f"Event: {evt}")
        if evt not in self.__alphabet:
            # print(f"Event {evt.get_name()} in supervisor {self.__name} is not defined.")
            return True
        last_state = self.__current_state
        for transition in self.__current_state.get_transitions():
            if transition.get_event() == evt:
                self.__current_state = transition.get_target()
                self.__last_state = last_state
                return True
        return False

    def get_enabled_events(self) -> List[Event]:
        """
        Returns the list of events that are enabled in the current state.

        Returns:
            list: List of enabled events.
        """
        return self.__current_state.get_enabled_events()

    def get_enabled_controllable_events(self) -> List[Event]:
        """
        Returns the list of controllable events that are enabled in the current state.

        Returns:
            list: List of enabled controllable events.
        """
        return self.__current_state.get_enabled_controllable_events()

    def get_alphabet(self) -> List[Event]:
        """
        Returns the list of events that the supervisor can handle.

        Returns:
            list: List of events.
        """
        return self.__alphabet

    def get_name(self):
        """
        Returns the name of the supervisor.

        Returns:
            str: The name of the supervisor.
        """
        return self.__name
    