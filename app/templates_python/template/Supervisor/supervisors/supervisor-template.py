"""
File with the creation, initialization and 
linking of supervisor structures
"""
# pylint: disable=C0103

from .. import Events, State, Supervisor

# Create states
%$%{states}

# Create transitions
%$%{transitions}

# create state list
state_list = []
%$%{state_list}

# create event list
alphabet = []
%$%{alphabet}

# create supervisor
%$%supervisor_name = Supervisor("%$%supervisor_name", state_list, alphabet)
