/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include "events.h"
#include "event_handler.h"
#include <stdio.h>

void on_action(const Event *event) { printf("\n\nON action\n\n"); }
void off_action(const Event *event) { printf("\n\nOFF action\n\n"); }

void setup() {
  printf("Start supervisor!\n\n");
  // set action on controllable events for example
  set_event_action(&on, on_action);
  set_event_action(&off, off_action);

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

void loop() {
  // handle events for teste
}

int app_main(void) {
  setup();
  // while (1) {
  //   loop();
  // }
  return 0;
}