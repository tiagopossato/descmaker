#include <assert.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

#include "supervisor.h"

void print_supervisor_alphabet(Supervisor *supervisor) {
  assert(supervisor != NULL);
  Alphabet *alphabet = supervisor->alphabet;
  SUP_DEBUG_PRINT("Alphabet: [");
  while (alphabet != NULL) {
    SUP_DEBUG_PRINT("%s%s", alphabet->event->name,
                    alphabet->next != NULL ? ", " : "]\n");
    // SUP_DEBUG_PRINT("Event %u: %s, \tthis:%p, next:%p\n",
    // alphabet->event->id,alphabet->event->name, alphabet, alphabet->next);
    alphabet = alphabet->next;
  }
}

bool run_supervisor(Supervisor *supervisor, Event *event) {
  assert(supervisor != NULL);
  assert(event != NULL);

  State *last_state = supervisor->current_state;
  Transition *transition = supervisor->current_state->transitions;
  while (transition != NULL) {
    if (transition->event->id == event->id) {
      supervisor->current_state = transition->target;
      supervisor->last_state = last_state;
      SUP_DEBUG_PRINT("%s, event %s %s => %s -> %s\n", supervisor->name,
                      event->kind == CONTROLLABLE ? SUP_DEBUG_STR("CONTROLLABLE")
                                                  : SUP_DEBUG_STR("UNCONTROLLABLE"),
                      event->name, supervisor->last_state->name,
                      supervisor->current_state->name);
      return true;
    }
    transition = transition->next;
  }
  return false;
}

void print_state(State *state) {
  assert(state != NULL);
  // print transitions for the initial state
  SUP_DEBUG_PRINT("[");
  Transition *transition = state->transitions;
  while (transition != NULL) {
    SUP_DEBUG_PRINT("%s->%s%s", transition->event->name,
                    transition->target->name,
                    transition->next != NULL ? ", " : "]\n");
    transition = transition->next;
  }
}

void set_event_callback(Event *event, EventCallback callback) {
  event->callback = callback;
}

void run_event_callback(Event *event) {
  if (event->callback != NULL) {
    event->callback(event);
  }
}

bool is_supervisor_event_enabled(Supervisor *supervisor, Event *event) {
  // if event is enabled in one transition return true
  Transition *transition = supervisor->current_state->transitions;
  while (transition != NULL) {
    if (transition->event->id == event->id) {
      return true;
    }
    transition = transition->next;
  }
  return false;
}

bool is_event_in_supervisor_alphabet(Supervisor *supervisor, Event *event) {
  // if event is in the alphabet return true
  Alphabet *alphabet = supervisor->alphabet;
  while (alphabet != NULL) {
    if (alphabet->event->id == event->id) {
      return true;
    }
    alphabet = alphabet->next;
  }
  return false;
}