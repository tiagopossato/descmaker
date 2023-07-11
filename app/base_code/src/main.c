/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include <stdio.h>
#include "../lib/supervisor/supervisor.h"
#include "supervisors/events.h"
#include "supervisors/handle_event.h"

void default_callback(Event *event) { printf("Default callback\n"); }

void setup(){
  printf("Start supervisor!\n\n");
  // set default callback for example
  set_event_callback(&btn, default_callback);
  
  set_event_callback(&liga, default_callback);
  set_event_callback(&desliga, default_callback);

  // handle events for teste
  handle_event(&btn);
  printf("\n-----------------------------------------\n");
  handle_event(&btn);
  printf("\n-----------------------------------------\n");
  handle_event(&btn);
  printf("\n-----------------------------------------\n");
  handle_event(&btn);
    printf("\n-----------------------------------------\n");
  handle_event(&btn);
}

void loop(){
  // handle events for teste
}

int main(void) {
  setup();
  // while (1) {
  //   loop();
  // }
  return 0;
}