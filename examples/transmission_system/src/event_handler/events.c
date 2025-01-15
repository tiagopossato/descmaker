#include <stdlib.h>
#include "events.h"
// create events
Event tran_1 = {CONTROLLABLE, 0, SUP_DEBUG_STR("tran_1"), NULL};
Event ack_1 = {UNCONTROLLABLE, 1, SUP_DEBUG_STR("ack_1"), NULL};
Event arr_1 = {UNCONTROLLABLE, 2, SUP_DEBUG_STR("arr_1"), NULL};
Event arr_2 = {UNCONTROLLABLE, 3, SUP_DEBUG_STR("arr_2"), NULL};
Event ack_2 = {UNCONTROLLABLE, 4, SUP_DEBUG_STR("ack_2"), NULL};
Event tran_2 = {CONTROLLABLE, 5, SUP_DEBUG_STR("tran_2"), NULL};

Event *controllable_event_list[CONTROLLABLE_EVENTS_COUNT] = {&tran_1,&tran_2};
