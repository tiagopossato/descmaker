#include <stdbool.h>
#include <stdlib.h>

#include "../event_handler/events.h"
#include "%$%{sup_name_source}.h"

// Supervisor specific instances
// alphabet create
%$%{alphabet_create_source}
// Alphabet init
%$%{alphabet_init_source}
// states create
%$%{state_create_source}
// transitions create and init
%$%{transitions_list_source}
// states init
%$%{state_init_source}
// Supervisor create
%$%{supervisor_create_source}