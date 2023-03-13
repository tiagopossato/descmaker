#include "handle_event.h"
#include "../../lib/supervisor/supervisor.h"
#include "events.h"
#include "sup.h"
#include <stdio.h>

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

// than recreate and linking them
SupervisorList sup_list = {&sup, NULL};

void handle_event(Event *event) {
  // check if event is enabled in all supervisors
  SupervisorList *sup = &sup_list;
  bool event_enabled = false;
  while (sup != NULL) {
    if (is_event_in_supervisor_alphabet(sup->supervisor, event)) {
      if (is_supervisor_event_enabled(sup->supervisor, event)) {
        event_enabled = true;
      } else {
        SUP_DEBUG_PRINT("Event %s is not enabled!\n", event->name);
        return;
      }
    }
    sup = sup->next;
  }

  if (event_enabled == false) {
    SUP_DEBUG_PRINT("Event %s is not in any supervisor alphabet!\n", event->name);
    return;
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

  // printf("Event %s handled!\n", event->name);
}