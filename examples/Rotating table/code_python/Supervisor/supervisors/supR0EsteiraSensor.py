from .. import Events, State, Supervisor

# Create states
S0_S0_S0_state = State("S0_S0_S0", True)
S0_S1_S0_state = State("S0_S1_S0", False)
S1_S0_S0_state = State("S1_S0_S0", False)
S1_S1_S0_state = State("S1_S1_S0", False)


# Create transitions
S0_S0_S0_state.add_transition(Events['se'], S1_S0_S0_state)
S0_S1_S0_state.add_transition(Events['b1'], S0_S0_S0_state)
S0_S1_S0_state.add_transition(Events['se'], S1_S1_S0_state)
S1_S0_S0_state.add_transition(Events['a1'], S0_S1_S0_state)
S1_S0_S0_state.add_transition(Events['se'], S1_S0_S0_state)
S1_S1_S0_state.add_transition(Events['b1'], S1_S0_S0_state)
S1_S1_S0_state.add_transition(Events['se'], S1_S1_S0_state)


# create state list
state_list = []
state_list.append(S0_S0_S0_state)
state_list.append(S0_S1_S0_state)
state_list.append(S1_S0_S0_state)
state_list.append(S1_S1_S0_state)


# create event list
alphabet = []
alphabet.append(Events['se'])
alphabet.append(Events['b1'])
alphabet.append(Events['a1'])


# create supervisor
supR0EsteiraSensor = Supervisor("supR0EsteiraSensor", state_list, alphabet)