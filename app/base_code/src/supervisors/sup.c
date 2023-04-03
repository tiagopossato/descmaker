#include <stdbool.h>
#include <stdlib.h>

#include "../../lib/supervisor/supervisor.h"

#include "events.h"
#include "sup.h"

// Supervisor specific instances
// alphabet create
Alphabet sup_btn_evt0;
Alphabet sup_desliga_evt1;
Alphabet sup_liga_evt2;

// Alphabet init
Alphabet sup_btn_evt0 = {&btn, &sup_desliga_evt1};
Alphabet sup_desliga_evt1 = {&desliga, &sup_liga_evt2};
Alphabet sup_liga_evt2 = {&liga, NULL};

// states create
State sup_G1S0_E1S0_E2S0_G2S0;
State sup_G1S0_E1S0_E2S0_G2S1;
State sup_G1S0_E1S0_E2S1_G2S1;
State sup_G1S0_E1S1_E2S0_G2S0;
State sup_G1S0_E1S1_E2S0_G2S1;
State sup_G1S0_E1S1_E2S1_G2S0;
State sup_G1S0_E1S1_E2S1_G2S1;

// transitions create and init
Transition sup_G1S0_E1S0_E2S0_G2S0_t0;
Transition sup_G1S0_E1S0_E2S0_G2S0_t0 = {&btn, &sup_G1S0_E1S1_E2S1_G2S0, NULL};

Transition sup_G1S0_E1S0_E2S0_G2S1_t0;
Transition sup_G1S0_E1S0_E2S0_G2S1_t1;
Transition sup_G1S0_E1S0_E2S0_G2S1_t0 = {&desliga, &sup_G1S0_E1S0_E2S0_G2S0, &sup_G1S0_E1S0_E2S0_G2S1_t1};
Transition sup_G1S0_E1S0_E2S0_G2S1_t1 = {&btn, &sup_G1S0_E1S1_E2S1_G2S1, NULL};

Transition sup_G1S0_E1S0_E2S1_G2S1_t0;
Transition sup_G1S0_E1S0_E2S1_G2S1_t0 = {&btn, &sup_G1S0_E1S1_E2S0_G2S1, NULL};

Transition sup_G1S0_E1S1_E2S0_G2S0_t0;
Transition sup_G1S0_E1S1_E2S0_G2S0_t1;
Transition sup_G1S0_E1S1_E2S0_G2S0_t0 = {&liga, &sup_G1S0_E1S0_E2S0_G2S1, &sup_G1S0_E1S1_E2S0_G2S0_t1};
Transition sup_G1S0_E1S1_E2S0_G2S0_t1 = {&btn, &sup_G1S0_E1S1_E2S1_G2S0, NULL};

Transition sup_G1S0_E1S1_E2S0_G2S1_t0;
Transition sup_G1S0_E1S1_E2S0_G2S1_t1;
Transition sup_G1S0_E1S1_E2S0_G2S1_t0 = {&desliga, &sup_G1S0_E1S1_E2S0_G2S0, &sup_G1S0_E1S1_E2S0_G2S1_t1};
Transition sup_G1S0_E1S1_E2S0_G2S1_t1 = {&btn, &sup_G1S0_E1S1_E2S1_G2S1, NULL};

Transition sup_G1S0_E1S1_E2S1_G2S0_t0;
Transition sup_G1S0_E1S1_E2S1_G2S0_t1;
Transition sup_G1S0_E1S1_E2S1_G2S0_t0 = {&liga, &sup_G1S0_E1S0_E2S1_G2S1, &sup_G1S0_E1S1_E2S1_G2S0_t1};
Transition sup_G1S0_E1S1_E2S1_G2S0_t1 = {&btn, &sup_G1S0_E1S1_E2S0_G2S0, NULL};

Transition sup_G1S0_E1S1_E2S1_G2S1_t0;
Transition sup_G1S0_E1S1_E2S1_G2S1_t0 = {&btn, &sup_G1S0_E1S1_E2S0_G2S1, NULL};


// states init
State sup_G1S0_E1S0_E2S0_G2S0 = {true, SUP_DEBUG_STR("G1S0_E1S0_E2S0_G2S0"), &sup_G1S0_E1S0_E2S0_G2S0_t0};
State sup_G1S0_E1S0_E2S0_G2S1 = {false, SUP_DEBUG_STR("G1S0_E1S0_E2S0_G2S1"), &sup_G1S0_E1S0_E2S0_G2S1_t0};
State sup_G1S0_E1S0_E2S1_G2S1 = {false, SUP_DEBUG_STR("G1S0_E1S0_E2S1_G2S1"), &sup_G1S0_E1S0_E2S1_G2S1_t0};
State sup_G1S0_E1S1_E2S0_G2S0 = {false, SUP_DEBUG_STR("G1S0_E1S1_E2S0_G2S0"), &sup_G1S0_E1S1_E2S0_G2S0_t0};
State sup_G1S0_E1S1_E2S0_G2S1 = {false, SUP_DEBUG_STR("G1S0_E1S1_E2S0_G2S1"), &sup_G1S0_E1S1_E2S0_G2S1_t0};
State sup_G1S0_E1S1_E2S1_G2S0 = {false, SUP_DEBUG_STR("G1S0_E1S1_E2S1_G2S0"), &sup_G1S0_E1S1_E2S1_G2S0_t0};
State sup_G1S0_E1S1_E2S1_G2S1 = {false, SUP_DEBUG_STR("G1S0_E1S1_E2S1_G2S1"), &sup_G1S0_E1S1_E2S1_G2S1_t0};

// Supervisor create
Supervisor sup = {&sup_G1S0_E1S0_E2S0_G2S0, &sup_G1S0_E1S0_E2S0_G2S0, NULL,  &sup_btn_evt0, "sup"};
