/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include <stdio.h>
#include "../lib/supervisor/supervisor.h"
#include "supervisors/events.h"
#include "supervisors/event_handler.h"

void default_action(Event *event) {
  printf("Action for %s event '%s'\n",
                  event->kind == CONTROLLABLE ? "CONTROLLABLE"
                                              : "UNCONTROLLABLE",
                  event->name);
}

void setup(){
  printf("Start supervisor!\n\n");
  // set action on controllable events for example
%$%{set_action}
  // trigger uncontrolable event for teste
%$%{trigger_event}
}

void loop(){
}

int main(void) {
  setup();
  // while (1) {
  //   loop();
  // }
  return 0;
}