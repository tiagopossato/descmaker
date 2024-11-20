/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include <stdio.h>
#include "events.h"
#include "event_handler.h"

void default_action(const Event *event) {
  SUP_DEBUG_PRINT("Action for %s event '%s'\n",
                  event->kind == CONTROLLABLE ? "CONTROLLABLE"
                                              : "UNCONTROLLABLE",
                  event->name);
}

void setup(){
  printf("Start supervisor!\n\n");
  // set action on controllable events for example
%$%{set_action}
}

void loop(){
    // trigger uncontrolable event for test
%$%{trigger_event}
}

int app_main(void) {
  setup();
  while (1) {
    loop();
    vTaskDelay(pdMS_TO_TICKS(1000));
  }
  return 0;
}