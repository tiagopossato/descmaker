# Generated code

The file `main.py` is the entry point of the generated code and the only file you need to change and run.

1. First, create an action function to be called by the event handler whenever a handled event is enabled. The action function must have the following signature:

    ```python
    def action(event: Event):
        # do something
    ```
    Note that the action function receives an event as its parameter, which is an object belonging to the Event class. This particular event is the one that was enabled in the supervisor and subsequently triggered the invocation of the action function.

    In the action function, you can trigger other events by calling the `trigger_event` function.:

    ```python
    trigger_event(Events['other_event_name'])
    ```

2. Then, set the action function to the event handler:

    ```python
    Events['event_name'].set_action(action)
    ```

3. Finally, when an event is received, run the event handler:

    ```python
    trigger_event(Events['event_name'])
    ```

    If the event is enabled in all supervisors, the action function will be called.

`Events` is a dictionary with all the events. This is defined in the file `Supervisor/events.py`.