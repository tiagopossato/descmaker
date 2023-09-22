#include <stdbool.h>
#include <stdlib.h>

#include "../event_handler/events.h"
#include "sup.h"

// Supervisor specific instances
// alphabet create
const Alphabet sup_btn_evt0;
const Alphabet sup_desliga_evt1;
const Alphabet sup_liga_evt2;

// Alphabet init
const Alphabet sup_btn_evt0 = {&btn, &sup_desliga_evt1};
const Alphabet sup_desliga_evt1 = {&desliga, &sup_liga_evt2};
const Alphabet sup_liga_evt2 = {&liga, NULL};

// states create
const State sup_G1S0_E1S0_G2S0;
const State sup_G1S0_E1S0_G2S1;
const State sup_G1S0_E1S1_G2S0;
const State sup_G1S0_E1S1_G2S1;

// Transitions create and init
const Transition sup_G1S0_E1S0_G2S0_t0;
const Transition sup_G1S0_E1S0_G2S0_t0 = {&btn, &sup_G1S0_E1S1_G2S0, NULL};

const Transition sup_G1S0_E1S0_G2S1_t0;
const Transition sup_G1S0_E1S0_G2S1_t1;
const Transition sup_G1S0_E1S0_G2S1_t0 = {&desliga, &sup_G1S0_E1S0_G2S0, &sup_G1S0_E1S0_G2S1_t1};
const Transition sup_G1S0_E1S0_G2S1_t1 = {&btn, &sup_G1S0_E1S1_G2S1, NULL};

const Transition sup_G1S0_E1S1_G2S0_t0;
const Transition sup_G1S0_E1S1_G2S0_t1;
const Transition sup_G1S0_E1S1_G2S0_t0 = {&btn, &sup_G1S0_E1S0_G2S0, &sup_G1S0_E1S1_G2S0_t1};
const Transition sup_G1S0_E1S1_G2S0_t1 = {&liga, &sup_G1S0_E1S1_G2S1, NULL};

const Transition sup_G1S0_E1S1_G2S1_t0;
const Transition sup_G1S0_E1S1_G2S1_t0 = {&btn, &sup_G1S0_E1S0_G2S1, NULL};


// states init
const State sup_G1S0_E1S0_G2S0 = {true, SUP_DEBUG_STR("G1S0_E1S0_G2S0"), &sup_G1S0_E1S0_G2S0_t0};
const State sup_G1S0_E1S0_G2S1 = {false, SUP_DEBUG_STR("G1S0_E1S0_G2S1"), &sup_G1S0_E1S0_G2S1_t0};
const State sup_G1S0_E1S1_G2S0 = {false, SUP_DEBUG_STR("G1S0_E1S1_G2S0"), &sup_G1S0_E1S1_G2S0_t0};
const State sup_G1S0_E1S1_G2S1 = {false, SUP_DEBUG_STR("G1S0_E1S1_G2S1"), &sup_G1S0_E1S1_G2S1_t0};

// Supervisor create
Supervisor sup = {&sup_G1S0_E1S0_G2S0, &sup_G1S0_E1S0_G2S0, NULL,  &sup_btn_evt0, "sup"};
