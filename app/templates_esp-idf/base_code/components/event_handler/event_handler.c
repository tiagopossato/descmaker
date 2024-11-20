#include <stdio.h>

#include "supervisor_list.h"
#include "event_handler.h"
#include "events.h"

bool is_event_enabled(const Event *event);
bool handle_event(const Event *event);

bool is_event_enabled(const Event *event) {
  // check if event is enabled in all supervisors
  SupervisorList *sup = &sup_list;
  bool event_enabled = false;
  while (sup != NULL) {
    if (is_event_in_supervisor_alphabet(sup->supervisor, event)) {
      if (is_supervisor_event_enabled(sup->supervisor, event)) {
        event_enabled = true;
      } else {
        SUP_DEBUG_PRINT("Event %s %s is not enabled in supervisor %s!\n",
                        event->kind == CONTROLLABLE
                            ? SUP_DEBUG_STR("CONTROLLABLE")
                            : SUP_DEBUG_STR("UNCONTROLLABLE"),
                        event->name, sup->supervisor->name);
        return false;
      }
    }
    sup = sup->next;
  }

  if (event_enabled == false) {
    SUP_DEBUG_PRINT("Event %s %s is not in any supervisor alphabet!\n",
                    event->kind == CONTROLLABLE
                        ? SUP_DEBUG_STR("CONTROLLABLE")
                        : SUP_DEBUG_STR("UNCONTROLLABLE"),
                    event->name);
  }

  return event_enabled;
}

bool handle_event(const Event *event) {
  SupervisorList *sup = &sup_list;
  SUP_DEBUG_PRINT("Handling the %s event '%s'\n",
                        event->kind == CONTROLLABLE
                            ? SUP_DEBUG_STR("CONTROLLABLE")
                            : SUP_DEBUG_STR("UNCONTROLLABLE"),
                  event->name);

  if (!is_event_enabled(event)) {
    return false;
  }
  // run all supervisors
  while (sup != NULL) {
    make_supervisor_transition(sup->supervisor, event);
    sup = sup->next;
  }

  return true;
}

bool trigger_event(const Event *event) {
  if (!handle_event(event)) {
    return false;
  }
  run_event_action(event);

  for (uint16_t i = 0; i < CONTROLLABLE_EVENTS_COUNT; i++) {
    // tries to execute the event. The handle_event function itself checks that
    // it is enabled on all other supervisors There's no need to build a list of
    // the events enabled in all the supervisors, because if it isn't enabled in
    // one supervisor, it won't be in the others
    if (trigger_event(controllable_event_list[i]) == true) {
      // if true, the event was executed successfully
      // thus, the supervisors have already been updated and there is no need to
      // continue execution
      break;
    } else {
      // if false, the event was not executed successfully
      // so the supervisors have not been updated and can be
      // continue execution
      continue;
    }
  }
  return true;
}
