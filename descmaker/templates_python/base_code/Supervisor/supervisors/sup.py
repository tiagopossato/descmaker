"""
Exemplo de supervisor gerado.
É substituído pelo maker.py na hora de converter o supervisor.
"""
from .. import Events, State, Supervisor

# Create states
G1S0_E1S0_G2S0_state = State("G1S0_E1S0_G2S0", True)
G1S0_E1S0_G2S1_state = State("G1S0_E1S0_G2S1", False)
G1S0_E1S1_G2S0_state = State("G1S0_E1S1_G2S0", False)
G1S0_E1S1_G2S1_state = State("G1S0_E1S1_G2S1", False)


# Create transitions
G1S0_E1S0_G2S0_state.add_transition(Events['btn'], G1S0_E1S1_G2S0_state)
G1S0_E1S0_G2S1_state.add_transition(Events['desliga'], G1S0_E1S0_G2S0_state)
G1S0_E1S0_G2S1_state.add_transition(Events['btn'], G1S0_E1S1_G2S1_state)
G1S0_E1S1_G2S0_state.add_transition(Events['btn'], G1S0_E1S0_G2S0_state)
G1S0_E1S1_G2S0_state.add_transition(Events['liga'], G1S0_E1S1_G2S1_state)
G1S0_E1S1_G2S1_state.add_transition(Events['btn'], G1S0_E1S0_G2S1_state)


# create state list
state_list = []
state_list.append(G1S0_E1S0_G2S0_state)
state_list.append(G1S0_E1S0_G2S1_state)
state_list.append(G1S0_E1S1_G2S0_state)
state_list.append(G1S0_E1S1_G2S1_state)


# create event list
alphabet = []
alphabet.append(Events['btn'])
alphabet.append(Events['desliga'])
alphabet.append(Events['liga'])


# create supervisor
sup = Supervisor("sup", state_list, alphabet)