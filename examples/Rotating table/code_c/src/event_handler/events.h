#ifndef __EVENTS_H__
#define __EVENTS_H__

#include <stdlib.h>

#include "../../lib/supervisor/supervisor.h"

#define CONTROLLABLE_EVENTS_COUNT 5

// create events
extern Event a1;
extern Event b1;
extern Event a2;
extern Event b2;
extern Event se;
extern Event a0;
extern Event b0;
extern Event a3;
extern Event a4;
extern Event b3;
extern Event b4;

extern Event *controllable_event_list[CONTROLLABLE_EVENTS_COUNT];

#endif // __EVENTS_H__