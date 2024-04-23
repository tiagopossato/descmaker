#include <stdbool.h>
#include <stdlib.h>

#include "../event_handler/events.h"
#include "supR0EsteiraSensor.h"

// Supervisor specific instances
// alphabet create
const Alphabet supR0EsteiraSensor_se_evt0;
const Alphabet supR0EsteiraSensor_b1_evt1;
const Alphabet supR0EsteiraSensor_a1_evt2;

// Alphabet init
const Alphabet supR0EsteiraSensor_se_evt0 = {&se, &supR0EsteiraSensor_b1_evt1};
const Alphabet supR0EsteiraSensor_b1_evt1 = {&b1, &supR0EsteiraSensor_a1_evt2};
const Alphabet supR0EsteiraSensor_a1_evt2 = {&a1, NULL};

// states create
const State supR0EsteiraSensor_S0_S0_S0;
const State supR0EsteiraSensor_S0_S1_S0;
const State supR0EsteiraSensor_S1_S0_S0;
const State supR0EsteiraSensor_S1_S1_S0;

// transitions create and init
const Transition supR0EsteiraSensor_S0_S0_S0_t0;
const Transition supR0EsteiraSensor_S0_S0_S0_t0 = {&se, &supR0EsteiraSensor_S1_S0_S0, NULL};

const Transition supR0EsteiraSensor_S0_S1_S0_t0;
const Transition supR0EsteiraSensor_S0_S1_S0_t1;
const Transition supR0EsteiraSensor_S0_S1_S0_t0 = {&b1, &supR0EsteiraSensor_S0_S0_S0, &supR0EsteiraSensor_S0_S1_S0_t1};
const Transition supR0EsteiraSensor_S0_S1_S0_t1 = {&se, &supR0EsteiraSensor_S1_S1_S0, NULL};

const Transition supR0EsteiraSensor_S1_S0_S0_t0;
const Transition supR0EsteiraSensor_S1_S0_S0_t1;
const Transition supR0EsteiraSensor_S1_S0_S0_t0 = {&a1, &supR0EsteiraSensor_S0_S1_S0, &supR0EsteiraSensor_S1_S0_S0_t1};
const Transition supR0EsteiraSensor_S1_S0_S0_t1 = {&se, &supR0EsteiraSensor_S1_S0_S0, NULL};

const Transition supR0EsteiraSensor_S1_S1_S0_t0;
const Transition supR0EsteiraSensor_S1_S1_S0_t1;
const Transition supR0EsteiraSensor_S1_S1_S0_t0 = {&b1, &supR0EsteiraSensor_S1_S0_S0, &supR0EsteiraSensor_S1_S1_S0_t1};
const Transition supR0EsteiraSensor_S1_S1_S0_t1 = {&se, &supR0EsteiraSensor_S1_S1_S0, NULL};


// states init
const State supR0EsteiraSensor_S0_S0_S0 = {true, SUP_DEBUG_STR("S0_S0_S0"), &supR0EsteiraSensor_S0_S0_S0_t0};
const State supR0EsteiraSensor_S0_S1_S0 = {false, SUP_DEBUG_STR("S0_S1_S0"), &supR0EsteiraSensor_S0_S1_S0_t0};
const State supR0EsteiraSensor_S1_S0_S0 = {false, SUP_DEBUG_STR("S1_S0_S0"), &supR0EsteiraSensor_S1_S0_S0_t0};
const State supR0EsteiraSensor_S1_S1_S0 = {false, SUP_DEBUG_STR("S1_S1_S0"), &supR0EsteiraSensor_S1_S1_S0_t0};

// Supervisor create
Supervisor supR0EsteiraSensor = {&supR0EsteiraSensor_S0_S0_S0, &supR0EsteiraSensor_S0_S0_S0, NULL,  &supR0EsteiraSensor_se_evt0, "supR0EsteiraSensor"};
