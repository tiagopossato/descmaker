/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include <stdio.h>
#include "event_handler/events.h"
#include "event_handler/event_handler.h"

void default_action(const Event *event) {
  printf("Action for %s event '%s'\n",
                  event->kind == CONTROLLABLE ? "CONTROLLABLE"
                                              : "UNCONTROLLABLE",
                  event->name);
}

void setup(){
  printf("Start supervisor!\n\n");
  // set action on controllable events for example
  set_event_action(&a1, default_action);
  set_event_action(&a2, default_action);
  set_event_action(&a0, default_action);
  set_event_action(&a3, default_action);
  set_event_action(&a4, default_action);

  // trigger uncontrolable event for teste
  trigger_event(&b1);
  trigger_event(&b2);
  trigger_event(&se);
  trigger_event(&b0);
  trigger_event(&b3);
  trigger_event(&b4);

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