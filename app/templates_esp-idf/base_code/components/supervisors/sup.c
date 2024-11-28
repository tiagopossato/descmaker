// Example code. It will be ignored by DEScMaker

#include "events.h"
#include "sup.h"
#include <stdbool.h>
#include <stdlib.h>

// Supervisor specific instances
// alphabet create
const Alphabet sup_btn_evt0;
const Alphabet sup_off_evt1;
const Alphabet sup_on_evt2;

// Alphabet init
const Alphabet sup_btn_evt0 = {&btn, &sup_off_evt1};
const Alphabet sup_off_evt1 = {&off, &sup_on_evt2};
const Alphabet sup_on_evt2 = {&on, NULL};

// states create
const State sup_G1S0_E1S0_G2S0;
const State sup_G1S0_E1S0_G2S1;
const State sup_G1S0_E1S1_G2S0;
const State sup_G1S0_E1S1_G2S1;

// transitions create and init
const Transition sup_G1S0_E1S0_G2S0_t0;
const Transition sup_G1S0_E1S0_G2S0_t0 = {&btn, &sup_G1S0_E1S1_G2S0, NULL};

const Transition sup_G1S0_E1S0_G2S1_t0;
const Transition sup_G1S0_E1S0_G2S1_t1;
const Transition sup_G1S0_E1S0_G2S1_t0 = {&off, &sup_G1S0_E1S0_G2S0, &sup_G1S0_E1S0_G2S1_t1};
const Transition sup_G1S0_E1S0_G2S1_t1 = {&btn, &sup_G1S0_E1S1_G2S1, NULL};

const Transition sup_G1S0_E1S1_G2S0_t0;
const Transition sup_G1S0_E1S1_G2S0_t1;
const Transition sup_G1S0_E1S1_G2S0_t0 = {&btn, &sup_G1S0_E1S0_G2S0, &sup_G1S0_E1S1_G2S0_t1};
const Transition sup_G1S0_E1S1_G2S0_t1 = {&on, &sup_G1S0_E1S1_G2S1, NULL};

const Transition sup_G1S0_E1S1_G2S1_t0;
const Transition sup_G1S0_E1S1_G2S1_t0 = {&btn, &sup_G1S0_E1S0_G2S1, NULL};


// states init
const State sup_G1S0_E1S0_G2S0 = {true, SUP_DEBUG_STR("G1S0_E1S0_G2S0"), &sup_G1S0_E1S0_G2S0_t0};
const State sup_G1S0_E1S0_G2S1 = {false, SUP_DEBUG_STR("G1S0_E1S0_G2S1"), &sup_G1S0_E1S0_G2S1_t0};
const State sup_G1S0_E1S1_G2S0 = {false, SUP_DEBUG_STR("G1S0_E1S1_G2S0"), &sup_G1S0_E1S1_G2S0_t0};
const State sup_G1S0_E1S1_G2S1 = {false, SUP_DEBUG_STR("G1S0_E1S1_G2S1"), &sup_G1S0_E1S1_G2S1_t0};

// Supervisor create
Supervisor sup = {(State *)&sup_G1S0_E1S0_G2S0, (State *)&sup_G1S0_E1S0_G2S0, NULL,  &sup_btn_evt0, "sup"};
