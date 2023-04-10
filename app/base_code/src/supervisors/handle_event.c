#include <stdio.h>
#include "events.h"
#include "handle_event.h"

#include "sup.h"



/**
 * @brief The alphabet
 */
typedef struct _SupervisorList SupervisorList;
struct _SupervisorList {
  Supervisor *supervisor;
  SupervisorList *next;
};

// make list with all supervisors
// first create all supervisors
extern SupervisorList sup_list;

// then recreate and linking them
SupervisorList sup_list = {&sup, NULL};

bool handle_event(Event *event) {
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
    return false;
  }
  // run all supervisors
  sup = &sup_list;
  while (sup != NULL) {
    if (is_event_in_supervisor_alphabet(sup->supervisor, event)) {
      run_supervisor(sup->supervisor, event);
    }
    sup = sup->next;
  }

  run_event_callback(event);

  return true;
}