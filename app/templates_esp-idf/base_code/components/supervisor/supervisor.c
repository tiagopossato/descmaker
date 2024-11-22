#include <assert.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

#include "supervisor.h"

void print_supervisor_alphabet(Supervisor *supervisor) {
  assert(supervisor != NULL);
  const Alphabet *alphabet = supervisor->alphabet;
  SUP_DEBUG_PRINT("Alphabet: [");
  while (alphabet != NULL) {
    SUP_DEBUG_PRINT("%s%s", alphabet->event->name,
                    alphabet->next != NULL ? ", " : "]\n");
    // SUP_DEBUG_PRINT("Event %u: %s, \tthis:%p, next:%p\n",
    // alphabet->event->id,alphabet->event->name, alphabet, alphabet->next);
    alphabet = alphabet->next;
  }
}

bool make_supervisor_transition(Supervisor *supervisor, const Event *event) {
  assert(supervisor != NULL);
  assert(event != NULL);

  State *last_state = supervisor->current_state;
  const Transition *transition = supervisor->current_state->transitions;

  if (!is_event_in_supervisor_alphabet(supervisor, event)) {
    return true;
  }

  while (transition != NULL) {
    if (transition->event->id == event->id) {
      supervisor->current_state = transition->target_state;
      supervisor->last_state = last_state;
      SUP_DEBUG_PRINT("%s, event %s %s => %s -> %s\n", supervisor->name,
                      event->kind == CONTROLLABLE
                          ? SUP_DEBUG_STR("CONTROLLABLE")
                          : SUP_DEBUG_STR("UNCONTROLLABLE"),
                      event->name, supervisor->last_state->name,
                      supervisor->current_state->name);
      return true;
    }
    transition = transition->next;
  }
  return false;
}

void print_state(const State *state) {
  assert(state != NULL);
  // print transitions for the initial state
  SUP_DEBUG_PRINT("[");
  const Transition *transition = state->transitions;
  while (transition != NULL) {
    SUP_DEBUG_PRINT("%s->%s%s", transition->event->name,
                    transition->target_state->name,
                    transition->next != NULL ? ", " : "]\n");
    transition = transition->next;
  }
}

void set_event_action(Event *event, EventAction action) {
  event->action = action;
}

void run_event_action(const Event *event) {
  if (event->action != NULL) {
    SUP_DEBUG_PRINT("Running action for %s event '%s'\n",
                        event->kind == CONTROLLABLE
                            ? SUP_DEBUG_STR("CONTROLLABLE")
                            : SUP_DEBUG_STR("UNCONTROLLABLE"),
                    event->name);
    event->action(event);
  }
}

bool is_supervisor_event_enabled(Supervisor *supervisor, const Event *event) {
  // if event is enabled in one transition return true
  const Transition *transition = supervisor->current_state->transitions;
  while (transition != NULL) {
    if (transition->event->id == event->id) {
      return true;
    }
    transition = transition->next;
  }
  return false;
}

bool is_event_in_supervisor_alphabet(Supervisor *supervisor,
                                     const Event *event) {
  // if event is in the alphabet return true
  const Alphabet *alphabet = supervisor->alphabet;
  while (alphabet != NULL) {
    if (alphabet->event->id == event->id) {
      return true;
    }
    alphabet = alphabet->next;
  }
  return false;
}

uint16_t get_enabled_controllable_events(Supervisor *supervisor,
                                         Event **events) {
  uint16_t i = 0;
  State *current_state = supervisor->current_state;
  const Transition *transition = current_state->transitions;
  while (transition != NULL) {
    if (transition->event->kind == CONTROLLABLE) {
      events[i] = transition->event;
      i++;
    }
    transition = transition->next;
  }
  return i;
}

void set_supervisor_to_initial_state(Supervisor *supervisor) {
  // Save last state
  supervisor->last_state = supervisor->current_state;
  // Puts fsm to initial state
  supervisor->current_state = supervisor->initial_state;
}