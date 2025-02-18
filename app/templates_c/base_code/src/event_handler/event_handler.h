#ifndef __HANDLE_EVENT_H__
#define __HANDLE_EVENT_H__

#include "../../lib/supervisor/supervisor.h"

#ifdef __cplusplus
extern "C" {
#endif

bool trigger_event(const Event *event);
void controller_start(void);

#ifdef __cplusplus
}
#endif

#endif // __HANDLE_EVENT_H__
