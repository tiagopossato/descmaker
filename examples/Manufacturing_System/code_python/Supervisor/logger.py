"""
Arquivo com funções para mostar eventos e estados do supervisor
Salva os logs em um arquivo csv
"""
from typing import List

# import depencies for log
from logging import Logger, StreamHandler, Formatter, FileHandler

from .Base import Event, Supervisor

# setup logger
logger = Logger("Supervisor")
#set file handler for persist log
file_handler = FileHandler("log.csv")
# set log handler for console
stream_handler = StreamHandler()

# set log format
formatter = Formatter("%(asctime)s; %(levelname)s; %(message)s")

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def log_error(event:Event, sup: Supervisor, msg: str):
    """
    Log error
    """
    try:
        logger.error(f"{event.get_name()}[{event.get_kind()}]; {sup.get_name()}; {sup.get_current_state().get_name()}; {msg}")
    except Exception as e:
        # verify if event is in Events dictionary
        if not isinstance(event, Event):
            raise TypeError("event must be instance of Event")
        # verify if supervisor is a Supervisor instance
        if not isinstance(sup, Supervisor):
            raise TypeError("supervisor must be instance of Supervisor")
        
        raise e

def log_state(event: Event, supervisors: List[Supervisor]):
    """
    Log state
    """
    try:
        # make log with list of transitions using last state and actual state
        transtions = "["
        for sup in supervisors:
            transtions += f"{sup.get_name()}: {sup.get_last_state().get_name()} -> {sup.get_current_state().get_name()}, "
        transtions = transtions[:-2] + "]"
        logger.info(f"{event.get_name()}; {transtions}")
        # logger.info(f"{event.get_name()}; [{', '.join([str(sup.get_last_state().get_name()) for sup in supervisors])}]")
    except Exception as e:
        # verify if event is in Events dictionary
        if not isinstance(event, Event):
            raise TypeError("event must be instance of Event")        
        # verify if states is a list of State instances
        if not isinstance(supervisors, List):
            raise TypeError("states must be a list")
        for state in supervisors:
            if not isinstance(state, Supervisor):
                raise TypeError("states must be a list of State instances")
        
        raise e