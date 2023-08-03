#include "event_handler.h"
#include "events.h"
#include <stdio.h>

#include "sup.h"

bool handle_event(Event *event);

// Event *event_list[TOTAL_CONTROLLABLE_EVENTS_COUNT];

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

bool trigger_event(Event *event) {
  if (!handle_event(event)) {
    return false;
  }
  run_event_callback(event);

  for (uint16_t i = 0; i < CONTROLLABLE_EVENTS_COUNT; i++) {

    printf("Automatically running the %s event '%s'\n",
           controllable_event_list[i]->kind == CONTROLLABLE ? "CONTROLLABLE"
                                                            : "UNCONTROLLABLE",
           controllable_event_list[i]->name);
    // tenta executar o evento. A própria função handle_event verifica se está
    // habilitado em todos os outros supervisores
    // Não é preciso montar uma lista dos eventos habilitados em todos os
    // supervisores, pois se não está habilitado em um supervisor, não
    // estará nos outros
    if (trigger_event(controllable_event_list[i]) == true) {
      // se retornar verdadeiro, o evento foi executado com sucesso
      // desta forma, os supervisores já foram atualizados e não deve-se
      // continuar a execução
      break;
    } else {
      // se retornar falso, o evento não foi executado com sucesso
      // desta forma, os supervisores não foram atualizados e pode-se
      // continuar a execução
      continue;
    }
  }
}

bool handle_event(Event *event) {
  // check if event is enabled in all supervisors
  SupervisorList *sup = &sup_list;
  bool event_enabled = false;
  while (sup != NULL) {
    if (is_event_in_supervisor_alphabet(sup->supervisor, event)) {
      if (is_supervisor_event_enabled(sup->supervisor, event)) {
        event_enabled = true;
      } else {
        SUP_DEBUG_PRINT("%s event '%s' is not enabled in supervisor %s!\n",
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
    SUP_DEBUG_PRINT("%s event %s is not in any supervisor alphabet!\n",
                    event->kind == CONTROLLABLE
                        ? SUP_DEBUG_STR("CONTROLLABLE")
                        : SUP_DEBUG_STR("UNCONTROLLABLE"),
                    event->name);
    return false;
  }
  // run all supervisors
  sup = &sup_list;
  while (sup != NULL) {
    run_supervisor(sup->supervisor, event);
    sup = sup->next;
  }

  return true;
}