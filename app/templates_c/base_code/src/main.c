/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include "event_handler/event_handler.h"
#include "event_handler/events.h"
#include <stdio.h>

void on_action(const Event *event) {
  printf("\n\nON action for %s event '%d'\n\n",
         event->kind == CONTROLLABLE ? "CONTROLLABLE" : "UNCONTROLLABLE",
         event->id);
}

void off_action(const Event *event) {
  printf("\n\nOFF action for %s event '%d'\n\n",
         event->kind == CONTROLLABLE ? "CONTROLLABLE" : "UNCONTROLLABLE",
         event->id);
}

void setup(void) {
  printf("Start supervisor!\n\n");
  // set action on controllable events for example
  set_event_action(&on, on_action);
  set_event_action(&off, off_action);

  // start the controller
  controller_start();

  // trigger uncontrolable event for test
  trigger_event(&btn);
  printf("\n-----------------------------------------\n");
  trigger_event(&btn);
  printf("\n-----------------------------------------\n");
  trigger_event(&btn);
  printf("\n-----------------------------------------\n");
  trigger_event(&btn);
  printf("\n-----------------------------------------\n");
}

int main(void) {
  setup();
  // while (1) {
  //   loop
  // }
  return 0;
}
