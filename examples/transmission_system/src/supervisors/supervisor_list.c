#include "supervisor_list.h"
#include "supervisor.h"

// make list with all supervisors
// first create all supervisors
extern SupervisorList supervisor_list;

// then recreate and linking them
SupervisorList sup_list = {&supervisor, NULL};

