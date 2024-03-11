"""
Classe para manipular os estados
"""
from typing import List

from .Event import Event
from .Transition import Transition

class State:
    def __init__(self, name: str, is_start: bool = False):
        if not isinstance(is_start, bool):
            raise TypeError("is_start must be a boolean")
        self.__is_start = is_start
        self.__name = name
        self.__transitions = []
    
    def add_transition(self, event: Event, target: "State"):
        """
        This function adds a new transition to the transitions list 
        if the same transition doesn't already exist. 
        If the same transition already exists, it prints a message indicating that. 
        The transition is created using the Transition class, 
        with the event and target state as parameters.

        Despite scanning all the state's transitions, 
        this method is only executed at the start of the application, 
        thus it doesn't impact overall performance."

        """
        if not isinstance(event, Event):
            raise TypeError("event must be instance of Event")
        if not isinstance(target,  type(self)):
            raise TypeError("target must be instance of State")

        if self.get_transition(event, target) is None:
            self.__transitions.append(Transition(event, target))
        else:
            print(f"Transition from state {self.name} to state {target.get_name()} \
                    with the event {event.get_name()} already exists.")

    def get_transition(self, event: Event, target):
        """
        This function searches the transitions list for a transition 
        with the specified event and target state. 
        If it finds the transition, it returns the transition. 
        Otherwise, it returns None.
        """
        if not isinstance(event, Event):
            raise TypeError("event must be instance of Event")        
        for transition in self.__transitions:
            if transition.get_event() == event and transition.get_target() == target:
                return transition
        return None

    def get_transitions(self)-> List[Transition]:
        return self.__transitions
    
    def get_enabled_events(self) -> List[Event]:
        return [tr.get_event() for tr in self.__transitions]
    
    def get_enabled_controllable_events(self) -> List[Event]:
        return [tr.get_event() for tr in self.__transitions if tr.get_event().is_controllable()]
    
    def get_name(self) -> str:
        return self.__name
    
    def is_start(self) -> bool:
        return self.__is_start
    