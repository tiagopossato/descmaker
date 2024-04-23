#include <stdbool.h>
#include <stdlib.h>

#include "../event_handler/events.h"
#include "supEsteiraMesa_GiratoriaR1.h"

// Supervisor specific instances
// alphabet create
const Alphabet supEsteiraMesa_GiratoriaR1_a0_evt0;
const Alphabet supEsteiraMesa_GiratoriaR1_a1_evt1;
const Alphabet supEsteiraMesa_GiratoriaR1_b0_evt2;
const Alphabet supEsteiraMesa_GiratoriaR1_b1_evt3;

// Alphabet init
const Alphabet supEsteiraMesa_GiratoriaR1_a0_evt0 = {&a0, &supEsteiraMesa_GiratoriaR1_a1_evt1};
const Alphabet supEsteiraMesa_GiratoriaR1_a1_evt1 = {&a1, &supEsteiraMesa_GiratoriaR1_b0_evt2};
const Alphabet supEsteiraMesa_GiratoriaR1_b0_evt2 = {&b0, &supEsteiraMesa_GiratoriaR1_b1_evt3};
const Alphabet supEsteiraMesa_GiratoriaR1_b1_evt3 = {&b1, NULL};

// states create
const State supEsteiraMesa_GiratoriaR1_S0_S0_S0;
const State supEsteiraMesa_GiratoriaR1_S0_S1_S1;
const State supEsteiraMesa_GiratoriaR1_S1_S0_S1;

// transitions create and init
const Transition supEsteiraMesa_GiratoriaR1_S0_S0_S0_t0;
const Transition supEsteiraMesa_GiratoriaR1_S0_S0_S0_t1;
const Transition supEsteiraMesa_GiratoriaR1_S0_S0_S0_t0 = {&a0, &supEsteiraMesa_GiratoriaR1_S0_S1_S1, &supEsteiraMesa_GiratoriaR1_S0_S0_S0_t1};
const Transition supEsteiraMesa_GiratoriaR1_S0_S0_S0_t1 = {&a1, &supEsteiraMesa_GiratoriaR1_S1_S0_S1, NULL};

const Transition supEsteiraMesa_GiratoriaR1_S0_S1_S1_t0;
const Transition supEsteiraMesa_GiratoriaR1_S0_S1_S1_t0 = {&b0, &supEsteiraMesa_GiratoriaR1_S0_S0_S0, NULL};

const Transition supEsteiraMesa_GiratoriaR1_S1_S0_S1_t0;
const Transition supEsteiraMesa_GiratoriaR1_S1_S0_S1_t0 = {&b1, &supEsteiraMesa_GiratoriaR1_S0_S0_S0, NULL};


// states init
const State supEsteiraMesa_GiratoriaR1_S0_S0_S0 = {true, SUP_DEBUG_STR("S0_S0_S0"), &supEsteiraMesa_GiratoriaR1_S0_S0_S0_t0};
const State supEsteiraMesa_GiratoriaR1_S0_S1_S1 = {false, SUP_DEBUG_STR("S0_S1_S1"), &supEsteiraMesa_GiratoriaR1_S0_S1_S1_t0};
const State supEsteiraMesa_GiratoriaR1_S1_S0_S1 = {false, SUP_DEBUG_STR("S1_S0_S1"), &supEsteiraMesa_GiratoriaR1_S1_S0_S1_t0};

// Supervisor create
Supervisor supEsteiraMesa_GiratoriaR1 = {&supEsteiraMesa_GiratoriaR1_S0_S0_S0, &supEsteiraMesa_GiratoriaR1_S0_S0_S0, NULL,  &supEsteiraMesa_GiratoriaR1_a0_evt0, "supEsteiraMesa_GiratoriaR1"};
