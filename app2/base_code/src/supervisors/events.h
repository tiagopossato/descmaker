#ifndef __EVENTS_H__
#define __EVENTS_H__

#include <stdint.h>

/**
 * @brief The event callback
 * @param event The event
 * @note The event callback should be set using setEventCallback
 */
typedef void (*EventCallback)(uint32_t event);

/**
 * @brief Set the event callback
 * @param event The event
 * @param callback The callback to set
 * @note The callback will be called when the event is triggered
 */
void set_event_callback(uint32_t event, EventCallback callback);

void run_event_callback(uint32_t event);

extern EventCallback eventsCallback;

// Definição dos eventos
#define btn 0
#define liga 1
#define desliga 2

#define NUM_EVENTS 3

#endif // __EVENTS_H__
