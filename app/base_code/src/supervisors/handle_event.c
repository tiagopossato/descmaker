#include "handle_event.h"
#include "events.h"
#include <stdio.h>

#include "sup.h"

Event *event_list[TOTAL_CONTROLLABLE_EVENTS_COUNT];

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

  // pega os eventos habilitados controláveis no primeiro supervisor da lista
  sup = &sup_list;
  uint16_t event_list_count =
      get_enabled_controllable_events(sup_list.supervisor, event_list);
  if (event_list_count > 0) {
    // print_event_list(event_list);
    for (uint16_t i = 0; i < event_list_count; i++) {
      printf("Rodando automaticamente o evento %s: %s\n", event_list[i]->name,
             event_list[i]->kind == CONTROLLABLE ? "CONTROLLABLE"
                                                 : "UNCONTROLLABLE");
      // tenta executar o evento. A própria função handle_event verifica se está
      // habilitado em todos os outros supervisores
      // Não é preciso montar uma lista dos eventos habilitados em todos os
      // supervisores, pois se não está habilidatado em um supervisor, não
      // estará nos outros
      if (handle_event(event_list[i]) == true) {
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
  return true;
}