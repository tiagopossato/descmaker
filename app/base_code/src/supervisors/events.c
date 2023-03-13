#include <stdlib.h>

#include "../../lib/supervisor/supervisor.h"
#include "events.h"

// create events
Event btnON = {UNCONTROLLABLE, 0, "btnON", NULL};
Event liga = {CONTROLLABLE, 1, "liga", NULL};
Event desliga = {CONTROLLABLE, 2, "desliga", NULL};