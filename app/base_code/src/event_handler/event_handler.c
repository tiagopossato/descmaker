#include <stdio.h>

#include "../supervisors/supervisor_list.h"
#include "event_handler.h"
#include "events.h"

bool is_event_enabled(Event *event);
bool handle_event(Event *event);

bool is_event_enabled(Event *event) {
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

bool handle_event(Event *event) {
  SupervisorList *sup = &sup_list;
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

bool trigger_event(Event *event) {
  if (!handle_event(event)) {
    return false;
  }
  SUP_DEBUG_PRINT("Running the %s event '%s'\n",
                  event->kind == CONTROLLABLE
                    ? "CONTROLLABLE"
                    : "UNCONTROLLABLE",
                  event->name);
  run_event_action(event);

  for (uint16_t i = 0; i < CONTROLLABLE_EVENTS_COUNT; i++) {
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