#ifndef __EVENTS_H__
#define __EVENTS_H__

#include <stdlib.h>

#include "../../lib/supervisor/supervisor.h"

#define CONTROLLABLE_EVENTS_COUNT 2

// create events
extern Event btn;
extern Event on;
extern Event off;

extern Event *controllable_event_list[CONTROLLABLE_EVENTS_COUNT];

#endif // __EVENTS_H__