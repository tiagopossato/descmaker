#ifndef __EVENTS_H__
#define __EVENTS_H__

#include "supervisor.h"
#include <stdlib.h>

#define CONTROLLABLE_EVENTS_COUNT %$%{events_controllable_count}

// create events
%$%{events_h}
extern Event *controllable_event_list[CONTROLLABLE_EVENTS_COUNT];

#endif // __EVENTS_H__
