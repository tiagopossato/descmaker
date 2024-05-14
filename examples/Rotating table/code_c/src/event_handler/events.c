#include <stdlib.h>
#include "events.h"
// create events
Event a1 = {CONTROLLABLE, 0, SUP_DEBUG_STR("a1"), NULL};
Event b1 = {UNCONTROLLABLE, 1, SUP_DEBUG_STR("b1"), NULL};
Event a2 = {CONTROLLABLE, 2, SUP_DEBUG_STR("a2"), NULL};
Event b2 = {UNCONTROLLABLE, 3, SUP_DEBUG_STR("b2"), NULL};
Event se = {UNCONTROLLABLE, 4, SUP_DEBUG_STR("se"), NULL};
Event a0 = {CONTROLLABLE, 5, SUP_DEBUG_STR("a0"), NULL};
Event b0 = {UNCONTROLLABLE, 6, SUP_DEBUG_STR("b0"), NULL};
Event a3 = {CONTROLLABLE, 7, SUP_DEBUG_STR("a3"), NULL};
Event a4 = {CONTROLLABLE, 8, SUP_DEBUG_STR("a4"), NULL};
Event b3 = {UNCONTROLLABLE, 9, SUP_DEBUG_STR("b3"), NULL};
Event b4 = {UNCONTROLLABLE, 10, SUP_DEBUG_STR("b4"), NULL};

Event *controllable_event_list[CONTROLLABLE_EVENTS_COUNT] = {&a1,&a2,&a0,&a3,&a4};