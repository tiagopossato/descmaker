/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include "../lib/supervisor/supervisor.h"
#include "supervisors/event_handler.h"
#include "supervisors/events.h"
#include <stdio.h>

void liga_callback(Event *event) { printf("\n\nLiga callback\n\n"); }
void desliga_callback(Event *event) { printf("\n\nDesliga callback\n\n"); }

void setup() {
  printf("Start supervisor!\n\n");
  // set callback on controllable events for example
  set_event_callback(&liga, liga_callback);
  set_event_callback(&desliga, desliga_callback);

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