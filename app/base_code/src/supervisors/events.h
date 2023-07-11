#ifndef __EVENTS_H__
#define __EVENTS_H__

#include <stdlib.h>

#include "../../lib/supervisor/supervisor.h"

#define TOTAL_CONTROLLABLE_EVENTS_COUNT 3

// create events
extern Event btn;
extern Event liga;
extern Event desliga;

#endif // __EVENTS_H__