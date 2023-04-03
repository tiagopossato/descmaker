#include <stdlib.h>

#include "../../lib/supervisor/supervisor.h"

// create events
Event btn = {UNCONTROLLABLE, 0, SUP_DEBUG_STR("btn"), NULL};
Event liga = {CONTROLLABLE, 1, SUP_DEBUG_STR("liga"), NULL};
Event desliga = {CONTROLLABLE, 2, SUP_DEBUG_STR("desliga"), NULL};
