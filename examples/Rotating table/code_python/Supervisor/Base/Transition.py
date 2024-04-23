"""
Classe para manipular as transições
"""
from . import Event
from . import State

class Transition:
    def __init__(self, event: Event, target: State):
        if not isinstance(event, Event):
            raise TypeError("event must be instance of Event")
        # if not isinstance(target, State):
        #     raise TypeError("target must be instance of State")
        
        self.__event = event
        self.__target = target
    
    def get_event(self) -> Event:
        return self.__event
    
    def get_target(self) -> State:
        return self.__target