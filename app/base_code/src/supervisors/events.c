#include <stdlib.h>

#include "../../lib/supervisor/supervisor.h"
#include "events.h"

// create events
Event btnON = {UNCONTROLLABLE, 0, SUP_DEBUG_STR("btnON"), NULL};
Event liga = {CONTROLLABLE, 1, SUP_DEBUG_STR("liga"), NULL};
Event desliga = {CONTROLLABLE, 2, SUP_DEBUG_STR("desliga"), NULL};