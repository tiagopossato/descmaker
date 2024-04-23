#include <stdbool.h>
#include <stdlib.h>

#include "../event_handler/events.h"
#include "supR2Mesa_GiratoriaFuradeira.h"

// Supervisor specific instances
// alphabet create
const Alphabet supR2Mesa_GiratoriaFuradeira_a2_evt0;
const Alphabet supR2Mesa_GiratoriaFuradeira_a0_evt1;
const Alphabet supR2Mesa_GiratoriaFuradeira_b2_evt2;
const Alphabet supR2Mesa_GiratoriaFuradeira_b0_evt3;

// Alphabet init
const Alphabet supR2Mesa_GiratoriaFuradeira_a2_evt0 = {&a2, &supR2Mesa_GiratoriaFuradeira_a0_evt1};
const Alphabet supR2Mesa_GiratoriaFuradeira_a0_evt1 = {&a0, &supR2Mesa_GiratoriaFuradeira_b2_evt2};
const Alphabet supR2Mesa_GiratoriaFuradeira_b2_evt2 = {&b2, &supR2Mesa_GiratoriaFuradeira_b0_evt3};
const Alphabet supR2Mesa_GiratoriaFuradeira_b0_evt3 = {&b0, NULL};

// states create
const State supR2Mesa_GiratoriaFuradeira_S0_S0_S0;
const State supR2Mesa_GiratoriaFuradeira_S1_S0_S1;
const State supR2Mesa_GiratoriaFuradeira_S1_S1_S0;

// transitions create and init
const Transition supR2Mesa_GiratoriaFuradeira_S0_S0_S0_t0;
const Transition supR2Mesa_GiratoriaFuradeira_S0_S0_S0_t1;
const Transition supR2Mesa_GiratoriaFuradeira_S0_S0_S0_t0 = {&a2, &supR2Mesa_GiratoriaFuradeira_S1_S0_S1, &supR2Mesa_GiratoriaFuradeira_S0_S0_S0_t1};
const Transition supR2Mesa_GiratoriaFuradeira_S0_S0_S0_t1 = {&a0, &supR2Mesa_GiratoriaFuradeira_S1_S1_S0, NULL};

const Transition supR2Mesa_GiratoriaFuradeira_S1_S0_S1_t0;
const Transition supR2Mesa_GiratoriaFuradeira_S1_S0_S1_t0 = {&b2, &supR2Mesa_GiratoriaFuradeira_S0_S0_S0, NULL};

const Transition supR2Mesa_GiratoriaFuradeira_S1_S1_S0_t0;
const Transition supR2Mesa_GiratoriaFuradeira_S1_S1_S0_t0 = {&b0, &supR2Mesa_GiratoriaFuradeira_S0_S0_S0, NULL};


// states init
const State supR2Mesa_GiratoriaFuradeira_S0_S0_S0 = {true, SUP_DEBUG_STR("S0_S0_S0"), &supR2Mesa_GiratoriaFuradeira_S0_S0_S0_t0};
const State supR2Mesa_GiratoriaFuradeira_S1_S0_S1 = {false, SUP_DEBUG_STR("S1_S0_S1"), &supR2Mesa_GiratoriaFuradeira_S1_S0_S1_t0};
const State supR2Mesa_GiratoriaFuradeira_S1_S1_S0 = {false, SUP_DEBUG_STR("S1_S1_S0"), &supR2Mesa_GiratoriaFuradeira_S1_S1_S0_t0};

// Supervisor create
Supervisor supR2Mesa_GiratoriaFuradeira = {&supR2Mesa_GiratoriaFuradeira_S0_S0_S0, &supR2Mesa_GiratoriaFuradeira_S0_S0_S0, NULL,  &supR2Mesa_GiratoriaFuradeira_a2_evt0, "supR2Mesa_GiratoriaFuradeira"};
