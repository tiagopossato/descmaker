// Example code. It will be overwritten by DEScMaker
#include "events.h"
#include <stdlib.h>
// create events
Event btn = {UNCONTROLLABLE, 0, SUP_DEBUG_STR("btn"), NULL};
Event on = {CONTROLLABLE, 1, SUP_DEBUG_STR("on"), NULL};
Event off = {CONTROLLABLE, 2, SUP_DEBUG_STR("off"), NULL};

Event *controllable_event_list[CONTROLLABLE_EVENTS_COUNT] = {&on, &off};
