Classes with the structures for the supervisor


## Event.py

The file ```Event.py``` contains the class ```Event``` which is used to store the information of an event. 

## Transition.py

The file ```Transition.py``` contains the class ```Transition``` which is used to store the information of a transition.

One transition is associated to one event and one state, named as ```target```.

## State.py

The file ```State.py``` contains the class ```State``` which is used to store the information of a state.

One ```State``` has a list of transitions. To add a transition to a state, use the method ```add_transition```, which receives an ```Event``` and a  ``` targe State``` as parameters.

## Supervisor.py

The file ```Supervisor.py``` contains the class ```Supervisor``` which is used to store the structure of a supervisor.

One ```Supervisor``` has a list of states, and a list of events.
Internally, the ```Supervisor``` store the start state and the current state.

The main method of the ```Supervisor``` is ```run``` which receives an ```Event``` as parameter and performs the transition to the next state, if the event is enabled.
