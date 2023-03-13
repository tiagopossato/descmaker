#include <assert.h>
#include <stdio.h>
#include "../../lib/supervisor/supervisor.h"
#include "events.h"
#include "handle_event.h"

%$%{handle_include_supervisors}


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
%$%{supervisor_list_create}
// then recreate and linking them
%$%{supervisor_list_init}
void handle_event(Event *event) {
  // check if event is enabled in all supervisors
  SupervisorList *sup = &%$%{supervisor_list_head};
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
  sup = &%$%{supervisor_list_head};
  while (sup != NULL) {
    if (is_event_in_supervisor_alphabet(sup->supervisor, event)) {
      run_supervisor(sup->supervisor, event);
    }
    sup = sup->next;
  }

  run_event_callback(event);

  // printf("Event %s handled!\n", event->name);
}