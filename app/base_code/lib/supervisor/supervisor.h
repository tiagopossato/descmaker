#ifndef __SUPERVISOR_H__
#define __SUPERVISOR_H__

#include <stdbool.h>
#include <stdint.h>

#include "sup_debug.h"

// abstract data types
typedef struct _Transition Transition;
typedef struct _Event Event;
typedef struct _State State;
typedef struct _Supervisor Supervisor;
typedef struct _Alphabet Alphabet;

/**
 * @brief The state
 */
struct _State {
  const bool is_start;
  const char *name;
  const Transition *transitions;
};

/**
 * @brief The alphabet
 */
struct _Alphabet {
  const Event *event;
  const Alphabet *next;
};

/**
 * @brief A transition
 */
struct _Transition {
  const Event *event;
  const State *target;
  const Transition *next;
};

/**
 * @brief The kind of event
 */
typedef enum EventKind { CONTROLLABLE, UNCONTROLLABLE } EventKind;

/**
 * @brief The event action
 * @param event The event
 * @note The event action should be set using setEventAction
 */
typedef void (*EventAction)(const Event *event);

/**
 * @brief An event
 * @note This struct should not be accessed directly.
 *      Declared here because dinamic allocation is not supported.
 *      Use the provided functions to access the event.
 */
struct _Event {
  const EventKind kind;
  const uint16_t id;
  const char *name;
  EventAction action;
};

/**
 * @brief The supervisor
 */
struct _Supervisor {
  const State *initial_state;
  State *current_state;
  State *last_state;
  const Alphabet *alphabet;
  const char *name;
};

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief Set the event action
 * @param event The event
 * @param action The action to set
 * @note The action will be called when the event is triggered
 */
void set_event_action(Event *event, EventAction action);

/**
 * @brief Run the event action
 * @param event The event
 * @note This function should only be called by the supervisor
 */
void run_event_action(const Event *event);

/**
 * Print the state and transitions
 */
void print_state(const State *state);

/**
 * Print the supervisor alphabet.
 * @param supervisor The supervisor.
 */
void print_supervisor_alphabet(Supervisor *supervisor);

/**
 * Check if the event is enabled in the current state of the supervisor.
 * @param supervisor The supervisor.
 * @param event The event to be checked.
 * @return True if the event is enabled, false otherwise.
 */
bool is_supervisor_event_enabled(Supervisor *supervisor, const Event *event);

/**
 * Check if the event is in the supervisor alphabet.
 * @param supervisor The supervisor.
 * @param event The event to be checked.
 * @return True if the event is in the alphabet, false otherwise.
 */
bool is_event_in_supervisor_alphabet(Supervisor *supervisor, const Event *event);

/**
 * Get the enabled controllable events in the current state of the supervisor.
 * @param supervisor The supervisor.
 * @param events The array of events to be filled.
 * @return The number of enabled controllable events.
 */
uint16_t get_enabled_controllable_events(Supervisor *supervisor,
                                         Event **events);

/**
 * Run the supervisor.
 * @param supervisor The supervisor.
 * @param event The event to be processed.
 * @return True if the event was processed, false otherwise.
 */
bool make_supervisor_transition(Supervisor *supervisor, const Event *event);
#ifdef __cplusplus
}
#endif

#endif // __SUPERVISOR_H__