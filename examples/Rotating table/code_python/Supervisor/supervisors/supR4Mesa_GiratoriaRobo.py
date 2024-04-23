from .. import Events, State, Supervisor

# Create states
S4_S0_S1_state = State("S4_S0_S1", False)
S4_S1_S0_state = State("S4_S1_S0", False)
S5_S0_S0_state = State("S5_S0_S0", True)


# Create transitions
S4_S0_S1_state.add_transition(Events['b4'], S5_S0_S0_state)
S4_S1_S0_state.add_transition(Events['b0'], S5_S0_S0_state)
S5_S0_S0_state.add_transition(Events['a4'], S4_S0_S1_state)
S5_S0_S0_state.add_transition(Events['a0'], S4_S1_S0_state)


# create state list
state_list = []
state_list.append(S4_S0_S1_state)
state_list.append(S4_S1_S0_state)
state_list.append(S5_S0_S0_state)


# create event list
alphabet = []
alphabet.append(Events['b4'])
alphabet.append(Events['b0'])
alphabet.append(Events['a4'])
alphabet.append(Events['a0'])


# create supervisor
supR4Mesa_GiratoriaRobo = Supervisor("supR4Mesa_GiratoriaRobo", state_list, alphabet)