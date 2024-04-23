#ifndef __SUPERVISOR_LIST_H__
#define __SUPERVISOR_LIST_H__

#include "../../lib/supervisor/supervisor.h"

/**
 * @brief The alphabet
 */
typedef struct _SupervisorList SupervisorList;
struct _SupervisorList {
  Supervisor *supervisor;
  SupervisorList *next;
};

// make list with all supervisors
// first create all supervisors
extern SupervisorList sup_list;

#endif // __SUPERVISOR_LIST_H__