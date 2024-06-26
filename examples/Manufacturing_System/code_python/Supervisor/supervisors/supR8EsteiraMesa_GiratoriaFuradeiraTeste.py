from .. import Events, State, Supervisor

# Create states
S0_S0_S0_S0_S0_state = State("S0_S0_S0_S0_S0", True)
S0_S0_S0_S0_S1_state = State("S0_S0_S0_S0_S1", False)
S0_S0_S0_S1_S0_state = State("S0_S0_S0_S1_S0", False)
S0_S0_S0_S1_S1_state = State("S0_S0_S0_S1_S1", False)
S0_S0_S1_S0_S0_state = State("S0_S0_S1_S0_S0", False)
S0_S0_S1_S0_S1_state = State("S0_S0_S1_S0_S1", False)
S0_S0_S1_S1_S0_state = State("S0_S0_S1_S1_S0", False)
S0_S0_S1_S1_S1_state = State("S0_S0_S1_S1_S1", False)
S0_S1_S0_S0_S0_state = State("S0_S1_S0_S0_S0", False)
S0_S1_S0_S0_S1_state = State("S0_S1_S0_S0_S1", False)
S0_S1_S0_S1_S0_state = State("S0_S1_S0_S1_S0", False)
S0_S1_S0_S1_S1_state = State("S0_S1_S0_S1_S1", False)
S0_S1_S1_S0_S0_state = State("S0_S1_S1_S0_S0", False)
S0_S1_S1_S0_S1_state = State("S0_S1_S1_S0_S1", False)
S0_S1_S1_S1_S0_state = State("S0_S1_S1_S1_S0", False)
S0_S1_S1_S1_S1_state = State("S0_S1_S1_S1_S1", False)
S1_S0_S0_S0_S0_state = State("S1_S0_S0_S0_S0", False)
S1_S0_S0_S0_S1_state = State("S1_S0_S0_S0_S1", False)
S1_S0_S0_S1_S0_state = State("S1_S0_S0_S1_S0", False)
S1_S0_S0_S1_S1_state = State("S1_S0_S0_S1_S1", False)
S1_S0_S1_S0_S0_state = State("S1_S0_S1_S0_S0", False)
S1_S0_S1_S0_S1_state = State("S1_S0_S1_S0_S1", False)
S1_S0_S1_S1_S0_state = State("S1_S0_S1_S1_S0", False)
S1_S0_S1_S1_S1_state = State("S1_S0_S1_S1_S1", False)
S1_S1_S0_S0_S0_state = State("S1_S1_S0_S0_S0", False)
S1_S1_S0_S0_S1_state = State("S1_S1_S0_S0_S1", False)
S1_S1_S0_S1_S0_state = State("S1_S1_S0_S1_S0", False)
S1_S1_S0_S1_S1_state = State("S1_S1_S0_S1_S1", False)
S1_S1_S1_S0_S0_state = State("S1_S1_S1_S0_S0", False)
S1_S1_S1_S0_S1_state = State("S1_S1_S1_S0_S1", False)
S1_S1_S1_S1_S0_state = State("S1_S1_S1_S1_S0", False)
S1_S1_S1_S1_S1_state = State("S1_S1_S1_S1_S1", False)


# Create transitions
S0_S0_S0_S0_S0_state.add_transition(Events['a3'], S0_S0_S0_S0_S1_state)
S0_S0_S0_S0_S0_state.add_transition(Events['a2'], S0_S0_S0_S1_S0_state)
S0_S0_S0_S0_S0_state.add_transition(Events['a1'], S0_S1_S0_S0_S0_state)
S0_S0_S0_S0_S1_state.add_transition(Events['a2'], S0_S0_S0_S1_S1_state)
S0_S0_S0_S0_S1_state.add_transition(Events['a1'], S0_S1_S0_S0_S1_state)
S0_S0_S0_S0_S1_state.add_transition(Events['b3'], S1_S0_S0_S0_S0_state)
S0_S0_S0_S1_S0_state.add_transition(Events['a3'], S0_S0_S0_S1_S1_state)
S0_S0_S0_S1_S0_state.add_transition(Events['a1'], S0_S1_S0_S1_S0_state)
S0_S0_S0_S1_S0_state.add_transition(Events['b2'], S1_S0_S0_S0_S0_state)
S0_S0_S0_S1_S1_state.add_transition(Events['a1'], S0_S1_S0_S1_S1_state)
S0_S0_S0_S1_S1_state.add_transition(Events['b2'], S1_S0_S0_S0_S1_state)
S0_S0_S0_S1_S1_state.add_transition(Events['b3'], S1_S0_S0_S1_S0_state)
S0_S0_S1_S0_S0_state.add_transition(Events['b0'], S0_S0_S0_S0_S0_state)
S0_S0_S1_S0_S0_state.add_transition(Events['a3'], S0_S0_S1_S0_S1_state)
S0_S0_S1_S0_S0_state.add_transition(Events['a2'], S0_S0_S1_S1_S0_state)
S0_S0_S1_S0_S0_state.add_transition(Events['a1'], S0_S1_S1_S0_S0_state)
S0_S0_S1_S0_S1_state.add_transition(Events['b0'], S0_S0_S0_S0_S1_state)
S0_S0_S1_S0_S1_state.add_transition(Events['a2'], S0_S0_S1_S1_S1_state)
S0_S0_S1_S0_S1_state.add_transition(Events['a1'], S0_S1_S1_S0_S1_state)
S0_S0_S1_S0_S1_state.add_transition(Events['b3'], S1_S0_S1_S0_S0_state)
S0_S0_S1_S1_S0_state.add_transition(Events['b0'], S0_S0_S0_S1_S0_state)
S0_S0_S1_S1_S0_state.add_transition(Events['a3'], S0_S0_S1_S1_S1_state)
S0_S0_S1_S1_S0_state.add_transition(Events['a1'], S0_S1_S1_S1_S0_state)
S0_S0_S1_S1_S0_state.add_transition(Events['b2'], S1_S0_S1_S0_S0_state)
S0_S0_S1_S1_S1_state.add_transition(Events['b0'], S0_S0_S0_S1_S1_state)
S0_S0_S1_S1_S1_state.add_transition(Events['a1'], S0_S1_S1_S1_S1_state)
S0_S0_S1_S1_S1_state.add_transition(Events['b2'], S1_S0_S1_S0_S1_state)
S0_S0_S1_S1_S1_state.add_transition(Events['b3'], S1_S0_S1_S1_S0_state)
S0_S1_S0_S0_S0_state.add_transition(Events['a3'], S0_S1_S0_S0_S1_state)
S0_S1_S0_S0_S0_state.add_transition(Events['a2'], S0_S1_S0_S1_S0_state)
S0_S1_S0_S0_S0_state.add_transition(Events['b1'], S1_S0_S0_S0_S0_state)
S0_S1_S0_S0_S1_state.add_transition(Events['a2'], S0_S1_S0_S1_S1_state)
S0_S1_S0_S0_S1_state.add_transition(Events['b1'], S1_S0_S0_S0_S1_state)
S0_S1_S0_S0_S1_state.add_transition(Events['b3'], S1_S1_S0_S0_S0_state)
S0_S1_S0_S1_S0_state.add_transition(Events['a3'], S0_S1_S0_S1_S1_state)
S0_S1_S0_S1_S0_state.add_transition(Events['b1'], S1_S0_S0_S1_S0_state)
S0_S1_S0_S1_S0_state.add_transition(Events['b2'], S1_S1_S0_S0_S0_state)
S0_S1_S0_S1_S1_state.add_transition(Events['b1'], S1_S0_S0_S1_S1_state)
S0_S1_S0_S1_S1_state.add_transition(Events['b2'], S1_S1_S0_S0_S1_state)
S0_S1_S0_S1_S1_state.add_transition(Events['b3'], S1_S1_S0_S1_S0_state)
S0_S1_S1_S0_S0_state.add_transition(Events['b0'], S0_S1_S0_S0_S0_state)
S0_S1_S1_S0_S0_state.add_transition(Events['a3'], S0_S1_S1_S0_S1_state)
S0_S1_S1_S0_S0_state.add_transition(Events['a2'], S0_S1_S1_S1_S0_state)
S0_S1_S1_S0_S0_state.add_transition(Events['b1'], S1_S0_S1_S0_S0_state)
S0_S1_S1_S0_S1_state.add_transition(Events['b0'], S0_S1_S0_S0_S1_state)
S0_S1_S1_S0_S1_state.add_transition(Events['a2'], S0_S1_S1_S1_S1_state)
S0_S1_S1_S0_S1_state.add_transition(Events['b1'], S1_S0_S1_S0_S1_state)
S0_S1_S1_S0_S1_state.add_transition(Events['b3'], S1_S1_S1_S0_S0_state)
S0_S1_S1_S1_S0_state.add_transition(Events['b0'], S0_S1_S0_S1_S0_state)
S0_S1_S1_S1_S0_state.add_transition(Events['a3'], S0_S1_S1_S1_S1_state)
S0_S1_S1_S1_S0_state.add_transition(Events['b1'], S1_S0_S1_S1_S0_state)
S0_S1_S1_S1_S0_state.add_transition(Events['b2'], S1_S1_S1_S0_S0_state)
S0_S1_S1_S1_S1_state.add_transition(Events['b0'], S0_S1_S0_S1_S1_state)
S0_S1_S1_S1_S1_state.add_transition(Events['b1'], S1_S0_S1_S1_S1_state)
S0_S1_S1_S1_S1_state.add_transition(Events['b2'], S1_S1_S1_S0_S1_state)
S0_S1_S1_S1_S1_state.add_transition(Events['b3'], S1_S1_S1_S1_S0_state)
S1_S0_S0_S0_S0_state.add_transition(Events['a0'], S0_S0_S1_S0_S0_state)
S1_S0_S0_S0_S0_state.add_transition(Events['a3'], S1_S0_S0_S0_S1_state)
S1_S0_S0_S0_S0_state.add_transition(Events['a2'], S1_S0_S0_S1_S0_state)
S1_S0_S0_S0_S0_state.add_transition(Events['a1'], S1_S1_S0_S0_S0_state)
S1_S0_S0_S0_S1_state.add_transition(Events['a0'], S0_S0_S1_S0_S1_state)
S1_S0_S0_S0_S1_state.add_transition(Events['b3'], S1_S0_S0_S0_S0_state)
S1_S0_S0_S0_S1_state.add_transition(Events['a2'], S1_S0_S0_S1_S1_state)
S1_S0_S0_S0_S1_state.add_transition(Events['a1'], S1_S1_S0_S0_S1_state)
S1_S0_S0_S1_S0_state.add_transition(Events['a0'], S0_S0_S1_S1_S0_state)
S1_S0_S0_S1_S0_state.add_transition(Events['b2'], S1_S0_S0_S0_S0_state)
S1_S0_S0_S1_S0_state.add_transition(Events['a3'], S1_S0_S0_S1_S1_state)
S1_S0_S0_S1_S0_state.add_transition(Events['a1'], S1_S1_S0_S1_S0_state)
S1_S0_S0_S1_S1_state.add_transition(Events['a0'], S0_S0_S1_S1_S1_state)
S1_S0_S0_S1_S1_state.add_transition(Events['b2'], S1_S0_S0_S0_S1_state)
S1_S0_S0_S1_S1_state.add_transition(Events['b3'], S1_S0_S0_S1_S0_state)
S1_S0_S0_S1_S1_state.add_transition(Events['a1'], S1_S1_S0_S1_S1_state)
S1_S0_S1_S0_S0_state.add_transition(Events['b0'], S1_S0_S0_S0_S0_state)
S1_S0_S1_S0_S0_state.add_transition(Events['a3'], S1_S0_S1_S0_S1_state)
S1_S0_S1_S0_S0_state.add_transition(Events['a2'], S1_S0_S1_S1_S0_state)
S1_S0_S1_S0_S0_state.add_transition(Events['a1'], S1_S1_S1_S0_S0_state)
S1_S0_S1_S0_S1_state.add_transition(Events['b0'], S1_S0_S0_S0_S1_state)
S1_S0_S1_S0_S1_state.add_transition(Events['b3'], S1_S0_S1_S0_S0_state)
S1_S0_S1_S0_S1_state.add_transition(Events['a2'], S1_S0_S1_S1_S1_state)
S1_S0_S1_S0_S1_state.add_transition(Events['a1'], S1_S1_S1_S0_S1_state)
S1_S0_S1_S1_S0_state.add_transition(Events['b0'], S1_S0_S0_S1_S0_state)
S1_S0_S1_S1_S0_state.add_transition(Events['b2'], S1_S0_S1_S0_S0_state)
S1_S0_S1_S1_S0_state.add_transition(Events['a3'], S1_S0_S1_S1_S1_state)
S1_S0_S1_S1_S0_state.add_transition(Events['a1'], S1_S1_S1_S1_S0_state)
S1_S0_S1_S1_S1_state.add_transition(Events['b0'], S1_S0_S0_S1_S1_state)
S1_S0_S1_S1_S1_state.add_transition(Events['b2'], S1_S0_S1_S0_S1_state)
S1_S0_S1_S1_S1_state.add_transition(Events['b3'], S1_S0_S1_S1_S0_state)
S1_S0_S1_S1_S1_state.add_transition(Events['a1'], S1_S1_S1_S1_S1_state)
S1_S1_S0_S0_S0_state.add_transition(Events['a0'], S0_S1_S1_S0_S0_state)
S1_S1_S0_S0_S0_state.add_transition(Events['b1'], S1_S0_S0_S0_S0_state)
S1_S1_S0_S0_S0_state.add_transition(Events['a3'], S1_S1_S0_S0_S1_state)
S1_S1_S0_S0_S0_state.add_transition(Events['a2'], S1_S1_S0_S1_S0_state)
S1_S1_S0_S0_S1_state.add_transition(Events['a0'], S0_S1_S1_S0_S1_state)
S1_S1_S0_S0_S1_state.add_transition(Events['b1'], S1_S0_S0_S0_S1_state)
S1_S1_S0_S0_S1_state.add_transition(Events['b3'], S1_S1_S0_S0_S0_state)
S1_S1_S0_S0_S1_state.add_transition(Events['a2'], S1_S1_S0_S1_S1_state)
S1_S1_S0_S1_S0_state.add_transition(Events['a0'], S0_S1_S1_S1_S0_state)
S1_S1_S0_S1_S0_state.add_transition(Events['b1'], S1_S0_S0_S1_S0_state)
S1_S1_S0_S1_S0_state.add_transition(Events['b2'], S1_S1_S0_S0_S0_state)
S1_S1_S0_S1_S0_state.add_transition(Events['a3'], S1_S1_S0_S1_S1_state)
S1_S1_S0_S1_S1_state.add_transition(Events['a0'], S0_S1_S1_S1_S1_state)
S1_S1_S0_S1_S1_state.add_transition(Events['b1'], S1_S0_S0_S1_S1_state)
S1_S1_S0_S1_S1_state.add_transition(Events['b2'], S1_S1_S0_S0_S1_state)
S1_S1_S0_S1_S1_state.add_transition(Events['b3'], S1_S1_S0_S1_S0_state)
S1_S1_S1_S0_S0_state.add_transition(Events['b1'], S1_S0_S1_S0_S0_state)
S1_S1_S1_S0_S0_state.add_transition(Events['b0'], S1_S1_S0_S0_S0_state)
S1_S1_S1_S0_S0_state.add_transition(Events['a3'], S1_S1_S1_S0_S1_state)
S1_S1_S1_S0_S0_state.add_transition(Events['a2'], S1_S1_S1_S1_S0_state)
S1_S1_S1_S0_S1_state.add_transition(Events['b1'], S1_S0_S1_S0_S1_state)
S1_S1_S1_S0_S1_state.add_transition(Events['b0'], S1_S1_S0_S0_S1_state)
S1_S1_S1_S0_S1_state.add_transition(Events['b3'], S1_S1_S1_S0_S0_state)
S1_S1_S1_S0_S1_state.add_transition(Events['a2'], S1_S1_S1_S1_S1_state)
S1_S1_S1_S1_S0_state.add_transition(Events['b1'], S1_S0_S1_S1_S0_state)
S1_S1_S1_S1_S0_state.add_transition(Events['b0'], S1_S1_S0_S1_S0_state)
S1_S1_S1_S1_S0_state.add_transition(Events['b2'], S1_S1_S1_S0_S0_state)
S1_S1_S1_S1_S0_state.add_transition(Events['a3'], S1_S1_S1_S1_S1_state)
S1_S1_S1_S1_S1_state.add_transition(Events['b1'], S1_S0_S1_S1_S1_state)
S1_S1_S1_S1_S1_state.add_transition(Events['b0'], S1_S1_S0_S1_S1_state)
S1_S1_S1_S1_S1_state.add_transition(Events['b2'], S1_S1_S1_S0_S1_state)
S1_S1_S1_S1_S1_state.add_transition(Events['b3'], S1_S1_S1_S1_S0_state)


# create state list
state_list = []
state_list.append(S0_S0_S0_S0_S0_state)
state_list.append(S0_S0_S0_S0_S1_state)
state_list.append(S0_S0_S0_S1_S0_state)
state_list.append(S0_S0_S0_S1_S1_state)
state_list.append(S0_S0_S1_S0_S0_state)
state_list.append(S0_S0_S1_S0_S1_state)
state_list.append(S0_S0_S1_S1_S0_state)
state_list.append(S0_S0_S1_S1_S1_state)
state_list.append(S0_S1_S0_S0_S0_state)
state_list.append(S0_S1_S0_S0_S1_state)
state_list.append(S0_S1_S0_S1_S0_state)
state_list.append(S0_S1_S0_S1_S1_state)
state_list.append(S0_S1_S1_S0_S0_state)
state_list.append(S0_S1_S1_S0_S1_state)
state_list.append(S0_S1_S1_S1_S0_state)
state_list.append(S0_S1_S1_S1_S1_state)
state_list.append(S1_S0_S0_S0_S0_state)
state_list.append(S1_S0_S0_S0_S1_state)
state_list.append(S1_S0_S0_S1_S0_state)
state_list.append(S1_S0_S0_S1_S1_state)
state_list.append(S1_S0_S1_S0_S0_state)
state_list.append(S1_S0_S1_S0_S1_state)
state_list.append(S1_S0_S1_S1_S0_state)
state_list.append(S1_S0_S1_S1_S1_state)
state_list.append(S1_S1_S0_S0_S0_state)
state_list.append(S1_S1_S0_S0_S1_state)
state_list.append(S1_S1_S0_S1_S0_state)
state_list.append(S1_S1_S0_S1_S1_state)
state_list.append(S1_S1_S1_S0_S0_state)
state_list.append(S1_S1_S1_S0_S1_state)
state_list.append(S1_S1_S1_S1_S0_state)
state_list.append(S1_S1_S1_S1_S1_state)


# create event list
alphabet = []
alphabet.append(Events['a3'])
alphabet.append(Events['a2'])
alphabet.append(Events['a1'])
alphabet.append(Events['b3'])
alphabet.append(Events['b2'])
alphabet.append(Events['b0'])
alphabet.append(Events['b1'])
alphabet.append(Events['a0'])


# create supervisor
supR8EsteiraMesa_GiratoriaFuradeiraTeste = Supervisor("supR8EsteiraMesa_GiratoriaFuradeiraTeste", state_list, alphabet)