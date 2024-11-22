#include <stdlib.h>
#include "events.h"
// create events
%$%{events_c}
Event *controllable_event_list[CONTROLLABLE_EVENTS_COUNT] = {%$%{controllable_event_list}};
