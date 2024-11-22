#include "supervisor_list.h"
%$%{handle_include_supervisors}
// make list with all supervisors
// first create all supervisors
%$%{supervisor_list_create}
// then recreate and linking them
%$%{supervisor_list_init}
