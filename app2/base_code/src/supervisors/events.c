#include "events.h"
#include <stdlib.h>

// Definição dos callbacks
EventCallback eventsCallback[NUM_EVENTS] = {NULL, NULL, NULL};

void set_event_callback(uint32_t event, EventCallback callback) {
  if (event < NUM_EVENTS) {
    eventsCallback[event] = callback;
  }
}

void run_event_callback(uint32_t event) {
  if (event < NUM_EVENTS) {
    if (eventsCallback[event] != NULL) {
      eventsCallback[event](event);
    }
  }
}