#ifndef __EVENTS_H__
#define __EVENTS_H__

#include <stdlib.h>

#include "../../lib/supervisor/supervisor.h"

#define CONTROLLABLE_EVENTS_COUNT 2

// create events
extern Event tran_1;
extern Event ack_1;
extern Event arr_1;
extern Event arr_2;
extern Event ack_2;
extern Event tran_2;

extern Event *controllable_event_list[CONTROLLABLE_EVENTS_COUNT];

#endif // __EVENTS_H__
