from .. import Events, State, Supervisor

# Create states
S0_S0_S0_state = State("S0_S0_S0", True)
S1_S0_S1_state = State("S1_S0_S1", False)
S1_S1_S0_state = State("S1_S1_S0", False)


# Create transitions
S0_S0_S0_state.add_transition(Events['a3'], S1_S0_S1_state)
S0_S0_S0_state.add_transition(Events['a0'], S1_S1_S0_state)
S1_S0_S1_state.add_transition(Events['b3'], S0_S0_S0_state)
S1_S1_S0_state.add_transition(Events['b0'], S0_S0_S0_state)


# create state list
state_list = []
state_list.append(S0_S0_S0_state)
state_list.append(S1_S0_S1_state)
state_list.append(S1_S1_S0_state)


# create event list
alphabet = []
alphabet.append(Events['a3'])
alphabet.append(Events['a0'])
alphabet.append(Events['b3'])
alphabet.append(Events['b0'])


# create supervisor
supR3Mesa_GiratoriaTeste = Supervisor("supR3Mesa_GiratoriaTeste", state_list, alphabet)