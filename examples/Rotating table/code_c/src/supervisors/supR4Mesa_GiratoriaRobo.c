#include <stdbool.h>
#include <stdlib.h>

#include "../event_handler/events.h"
#include "supR4Mesa_GiratoriaRobo.h"

// Supervisor specific instances
// alphabet create
const Alphabet supR4Mesa_GiratoriaRobo_b4_evt0;
const Alphabet supR4Mesa_GiratoriaRobo_b0_evt1;
const Alphabet supR4Mesa_GiratoriaRobo_a4_evt2;
const Alphabet supR4Mesa_GiratoriaRobo_a0_evt3;

// Alphabet init
const Alphabet supR4Mesa_GiratoriaRobo_b4_evt0 = {&b4, &supR4Mesa_GiratoriaRobo_b0_evt1};
const Alphabet supR4Mesa_GiratoriaRobo_b0_evt1 = {&b0, &supR4Mesa_GiratoriaRobo_a4_evt2};
const Alphabet supR4Mesa_GiratoriaRobo_a4_evt2 = {&a4, &supR4Mesa_GiratoriaRobo_a0_evt3};
const Alphabet supR4Mesa_GiratoriaRobo_a0_evt3 = {&a0, NULL};

// states create
const State supR4Mesa_GiratoriaRobo_S4_S0_S1;
const State supR4Mesa_GiratoriaRobo_S4_S1_S0;
const State supR4Mesa_GiratoriaRobo_S5_S0_S0;

// transitions create and init
const Transition supR4Mesa_GiratoriaRobo_S4_S0_S1_t0;
const Transition supR4Mesa_GiratoriaRobo_S4_S0_S1_t0 = {&b4, &supR4Mesa_GiratoriaRobo_S5_S0_S0, NULL};

const Transition supR4Mesa_GiratoriaRobo_S4_S1_S0_t0;
const Transition supR4Mesa_GiratoriaRobo_S4_S1_S0_t0 = {&b0, &supR4Mesa_GiratoriaRobo_S5_S0_S0, NULL};

const Transition supR4Mesa_GiratoriaRobo_S5_S0_S0_t0;
const Transition supR4Mesa_GiratoriaRobo_S5_S0_S0_t1;
const Transition supR4Mesa_GiratoriaRobo_S5_S0_S0_t0 = {&a4, &supR4Mesa_GiratoriaRobo_S4_S0_S1, &supR4Mesa_GiratoriaRobo_S5_S0_S0_t1};
const Transition supR4Mesa_GiratoriaRobo_S5_S0_S0_t1 = {&a0, &supR4Mesa_GiratoriaRobo_S4_S1_S0, NULL};


// states init
const State supR4Mesa_GiratoriaRobo_S4_S0_S1 = {false, SUP_DEBUG_STR("S4_S0_S1"), &supR4Mesa_GiratoriaRobo_S4_S0_S1_t0};
const State supR4Mesa_GiratoriaRobo_S4_S1_S0 = {false, SUP_DEBUG_STR("S4_S1_S0"), &supR4Mesa_GiratoriaRobo_S4_S1_S0_t0};
const State supR4Mesa_GiratoriaRobo_S5_S0_S0 = {true, SUP_DEBUG_STR("S5_S0_S0"), &supR4Mesa_GiratoriaRobo_S5_S0_S0_t0};

// Supervisor create
Supervisor supR4Mesa_GiratoriaRobo = {&supR4Mesa_GiratoriaRobo_S5_S0_S0, &supR4Mesa_GiratoriaRobo_S5_S0_S0, NULL,  &supR4Mesa_GiratoriaRobo_b4_evt0, "supR4Mesa_GiratoriaRobo"};
