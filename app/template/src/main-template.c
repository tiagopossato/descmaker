/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include <stdio.h>
#include "../lib/supervisor/supervisor.h"
#include "supervisors/events.h"
#include "supervisors/handle_event.h"
%$%{include_supervisors}

void default_callback(Event *event) { printf("Default callback\n"); }

void setup(){
  printf("Start supervisor!\n\n");
  // set default callback for example
%$%{set_callback}
  // handle events for teste
%$%{handle_event}
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