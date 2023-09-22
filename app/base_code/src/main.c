/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include "event_handler/events.h"
#include "event_handler/event_handler.h"
#include <stdio.h>

void liga_action(const Event *event) { printf("\n\nLiga action\n\n"); }
void desliga_action(const Event *event) { printf("\n\nDesliga action\n\n"); }

void setup() {
  printf("Start supervisor!\n\n");
  // set action on controllable events for example
  set_event_action(&liga, liga_action);
  set_event_action(&desliga, desliga_action);

  // trigger uncontrolable event for teste
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

int main(void) {
  setup();
  // while (1) {
  //   loop();
  // }
  return 0;
}