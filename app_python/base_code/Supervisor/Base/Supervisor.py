"""
Classe para manipular o supervisor
"""
from . import State
from . import Event
from typing import List

class Supervisor:
    def __init__(self, _name: str, _statesList: List[State], _alphabet: List[Event]):
        if not all(isinstance(x, State) for x in _statesList):
            raise TypeError("_statesList must be List[State]")
        
        if not all(isinstance(x, Event) for x in _alphabet):
            raise TypeError("_alphabet must be List[Event]")

        self.__name = _name
        self.__alphabet = _alphabet
        # verify if the states list have only one start state
        start_states = [state for state in _statesList if state.is_start()]
        if len(start_states) != 1:
            raise Exception("The states list must have only one start state.")
        
        self.__start = start_states[0]
        self.__current_state = self.__start
        self.__last_state = self.__start
        print(f"Starting supervisor {self.__name}. Start state: {self.__start.get_name()}")
        
    def get_start_state(self):
        return self.__start
    
    def get_current_state(self) -> State:
        return self.__current_state
    
    def get_last_state(self) -> State:
        return self.__last_state

    def run(self, evt: Event) -> bool:
        """
        Run the supervisor with the given event.
        """
        if not isinstance(evt, Event):
            raise TypeError("evt must be an Event")
        # print(f"Event: {evt}")
        if evt not in self.__alphabet:
            #print(f"Event {evt.get_name()} in supervisor {self.__name} is not defined.")
            return True
        last_state = self.__current_state
        for transition in self.__current_state.get_transitions():
            if transition.get_event() == evt:
                self.__current_state = transition.get_target()
                self.__last_state = last_state
                return True
        #print(f"Event {evt.get_name()} is not enabled in state {self.__current_state.get_name()}.")
        return False

    def get_enabled_events(self) -> List[Event]:
        return self.__current_state.get_enabled_events()
    
    def get_enabled_controllable_events(self) -> List[Event]:
        return self.__current_state.get_enabled_controllable_events()
    
    def get_alphabet(self) -> List[Event]:
        return self.__alphabet
    
    def get_name(self):
        return self.__name
