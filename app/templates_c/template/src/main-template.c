/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include "event_handler/event_handler.h"
#include "event_handler/events.h"
#include <stdio.h>

void default_action(const Event *event) {
  SUP_DEBUG_PRINT("Action for %s event '%s'\n",
                  event->kind == CONTROLLABLE ? "CONTROLLABLE"
                                              : "UNCONTROLLABLE",
                  event->name);
}

void setup(void) {
  printf("Start supervisor!\n\n");
  // set action on controllable events for example
%$%{set_action}
  // trigger uncontrolable event for teste
%$%{trigger_event}
}

int main(void) {
  setup();
  // while (1) {
  //   loop
  // }
  return 0;
}
