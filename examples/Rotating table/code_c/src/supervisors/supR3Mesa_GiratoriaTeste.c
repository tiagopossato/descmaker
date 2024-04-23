#include <stdbool.h>
#include <stdlib.h>

#include "../event_handler/events.h"
#include "supR3Mesa_GiratoriaTeste.h"

// Supervisor specific instances
// alphabet create
const Alphabet supR3Mesa_GiratoriaTeste_a3_evt0;
const Alphabet supR3Mesa_GiratoriaTeste_a0_evt1;
const Alphabet supR3Mesa_GiratoriaTeste_b3_evt2;
const Alphabet supR3Mesa_GiratoriaTeste_b0_evt3;

// Alphabet init
const Alphabet supR3Mesa_GiratoriaTeste_a3_evt0 = {&a3, &supR3Mesa_GiratoriaTeste_a0_evt1};
const Alphabet supR3Mesa_GiratoriaTeste_a0_evt1 = {&a0, &supR3Mesa_GiratoriaTeste_b3_evt2};
const Alphabet supR3Mesa_GiratoriaTeste_b3_evt2 = {&b3, &supR3Mesa_GiratoriaTeste_b0_evt3};
const Alphabet supR3Mesa_GiratoriaTeste_b0_evt3 = {&b0, NULL};

// states create
const State supR3Mesa_GiratoriaTeste_S0_S0_S0;
const State supR3Mesa_GiratoriaTeste_S1_S0_S1;
const State supR3Mesa_GiratoriaTeste_S1_S1_S0;

// transitions create and init
const Transition supR3Mesa_GiratoriaTeste_S0_S0_S0_t0;
const Transition supR3Mesa_GiratoriaTeste_S0_S0_S0_t1;
const Transition supR3Mesa_GiratoriaTeste_S0_S0_S0_t0 = {&a3, &supR3Mesa_GiratoriaTeste_S1_S0_S1, &supR3Mesa_GiratoriaTeste_S0_S0_S0_t1};
const Transition supR3Mesa_GiratoriaTeste_S0_S0_S0_t1 = {&a0, &supR3Mesa_GiratoriaTeste_S1_S1_S0, NULL};

const Transition supR3Mesa_GiratoriaTeste_S1_S0_S1_t0;
const Transition supR3Mesa_GiratoriaTeste_S1_S0_S1_t0 = {&b3, &supR3Mesa_GiratoriaTeste_S0_S0_S0, NULL};

const Transition supR3Mesa_GiratoriaTeste_S1_S1_S0_t0;
const Transition supR3Mesa_GiratoriaTeste_S1_S1_S0_t0 = {&b0, &supR3Mesa_GiratoriaTeste_S0_S0_S0, NULL};


// states init
const State supR3Mesa_GiratoriaTeste_S0_S0_S0 = {true, SUP_DEBUG_STR("S0_S0_S0"), &supR3Mesa_GiratoriaTeste_S0_S0_S0_t0};
const State supR3Mesa_GiratoriaTeste_S1_S0_S1 = {false, SUP_DEBUG_STR("S1_S0_S1"), &supR3Mesa_GiratoriaTeste_S1_S0_S1_t0};
const State supR3Mesa_GiratoriaTeste_S1_S1_S0 = {false, SUP_DEBUG_STR("S1_S1_S0"), &supR3Mesa_GiratoriaTeste_S1_S1_S0_t0};

// Supervisor create
Supervisor supR3Mesa_GiratoriaTeste = {&supR3Mesa_GiratoriaTeste_S0_S0_S0, &supR3Mesa_GiratoriaTeste_S0_S0_S0, NULL,  &supR3Mesa_GiratoriaTeste_a3_evt0, "supR3Mesa_GiratoriaTeste"};
