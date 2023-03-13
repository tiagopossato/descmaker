#include <stdbool.h>
#include <stdlib.h>

#include "../../lib/supervisor/supervisor.h"

#include "events.h"
#include "sup.h"

// Supervisor specific instances
// Alphabet init
Alphabet sup_btnON_evt0;
Alphabet sup_liga_evt1;
Alphabet sup_desliga_evt2;

// states create
State sup_q0;
State sup_q2;
State sup_q3;
State sup_q4;

// transitions create and init
Transition sup_q0_t0;
Transition sup_q2_t0;
Transition sup_q2_t1;
Transition sup_q3_t0;
Transition sup_q4_t0;
Transition sup_q4_t1;

Alphabet sup_btnON_evt0 = {&btnON, &sup_liga_evt1};
Alphabet sup_liga_evt1 = {&liga, &sup_desliga_evt2};
Alphabet sup_desliga_evt2 = {&desliga, NULL};

// transitions create and init
Transition sup_q0_t0 = {&btnON, &sup_q2, NULL};

Transition sup_q2_t0 = {&btnON, &sup_q2, &sup_q2_t1};
Transition sup_q2_t1 = {&liga, &sup_q3, NULL};

Transition sup_q3_t0 = {&btnON, &sup_q4, NULL};

Transition sup_q4_t0 = {&desliga, &sup_q0, &sup_q4_t1};
Transition sup_q4_t1 = {&btnON, &sup_q4, NULL};

// states init
State sup_q0 = {true, SUP_DEBUG_STR("q0"), &sup_q0_t0};
State sup_q2 = {false, SUP_DEBUG_STR("q2"), &sup_q2_t0};
State sup_q3 = {false, SUP_DEBUG_STR("q3"), &sup_q3_t0};
State sup_q4 = {false, SUP_DEBUG_STR("q4"), &sup_q4_t0};

// Supervisor create
Supervisor sup = {&sup_q0, &sup_q0, NULL,  &sup_btnON_evt0, "sup"};