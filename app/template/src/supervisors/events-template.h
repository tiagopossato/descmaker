#ifndef __EVENTS_H__
#define __EVENTS_H__

#include <stdlib.h>

#include "../../lib/supervisor/supervisor.h"

#define TOTAL_CONTROLLABLE_EVENTS_COUNT %$%{events_controllable_count}

// create events
%$%{events_h}
#endif // __EVENTS_H__