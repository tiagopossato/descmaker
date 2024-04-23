#include <stdbool.h>
#include <stdlib.h>

#include "../event_handler/events.h"
#include "supR7Mesa_GiratoriaTesteRobo.h"

// Supervisor specific instances
// alphabet create
const Alphabet supR7Mesa_GiratoriaTesteRobo_a4_evt0;
const Alphabet supR7Mesa_GiratoriaTesteRobo_b4_evt1;
const Alphabet supR7Mesa_GiratoriaTesteRobo_b0_evt2;
const Alphabet supR7Mesa_GiratoriaTesteRobo_a3_evt3;
const Alphabet supR7Mesa_GiratoriaTesteRobo_b3_evt4;
const Alphabet supR7Mesa_GiratoriaTesteRobo_a0_evt5;

// Alphabet init
const Alphabet supR7Mesa_GiratoriaTesteRobo_a4_evt0 = {&a4, &supR7Mesa_GiratoriaTesteRobo_b4_evt1};
const Alphabet supR7Mesa_GiratoriaTesteRobo_b4_evt1 = {&b4, &supR7Mesa_GiratoriaTesteRobo_b0_evt2};
const Alphabet supR7Mesa_GiratoriaTesteRobo_b0_evt2 = {&b0, &supR7Mesa_GiratoriaTesteRobo_a3_evt3};
const Alphabet supR7Mesa_GiratoriaTesteRobo_a3_evt3 = {&a3, &supR7Mesa_GiratoriaTesteRobo_b3_evt4};
const Alphabet supR7Mesa_GiratoriaTesteRobo_b3_evt4 = {&b3, &supR7Mesa_GiratoriaTesteRobo_a0_evt5};
const Alphabet supR7Mesa_GiratoriaTesteRobo_a0_evt5 = {&a0, NULL};

// states create
const State supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S0;
const State supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S1;
const State supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S0;
const State supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S1;
const State supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S0;
const State supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S1;
const State supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0;
const State supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S1;
const State supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0;
const State supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1;
const State supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0;
const State supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1;
const State supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0;
const State supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1;
const State supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0;
const State supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1;
const State supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S0;
const State supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1;
const State supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0;
const State supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1;
const State supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S0;
const State supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1;
const State supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S0;
const State supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S1;

// transitions create and init
const Transition supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S0_t0 = {&a4, &supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S1_t0 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S0_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S0_t0 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S0, &supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S0_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S0_t1 = {&a4, &supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S1_t0 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S1, &supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S1_t1 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S0_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S0_t0 = {&a3, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S0_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S0_t1 = {&a4, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S1_t0 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S0, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S1_t1 = {&a3, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0_t0 = {&b3, &supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S0, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0_t1 = {&a4, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S1_t0 = {&b3, &supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S1, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S1_t1 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0_t2;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0_t0 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S0, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0_t1 = {&a3, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0_t2};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0_t2 = {&a4, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1_t2;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1_t0 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S1, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1_t1 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1_t2};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1_t2 = {&a3, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0_t2;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0_t0 = {&b3, &supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S0, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0_t1 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0_t2};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0_t2 = {&a4, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1_t2;
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1_t0 = {&b3, &supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S1, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1_t1 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S1, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1_t2};
const Transition supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1_t2 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0_t0 = {&a3, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0_t1 = {&a0, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1_t2;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1_t0 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1_t1 = {&a3, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1_t2};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1_t2 = {&a0, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0_t0 = {&a0, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0_t1 = {&b3, &supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1_t2;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1_t0 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1_t1 = {&a0, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1_t2};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1_t2 = {&b3, &supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S0_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S0_t0 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S0_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S0_t1 = {&a3, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1_t2;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1_t0 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1_t1 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S0, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1_t2};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1_t2 = {&a3, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0_t0 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0_t1 = {&b3, &supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1_t2;
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1_t0 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1_t1 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0, &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1_t2};
const Transition supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1_t2 = {&b3, &supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S1, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S0_t0 = {&a0, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1_t0 = {&a0, &supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1, &supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1_t1 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S0_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S0_t0 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S0, NULL};

const Transition supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S1_t0;
const Transition supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S1_t1;
const Transition supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S1_t0 = {&b0, &supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1, &supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S1_t1};
const Transition supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S1_t1 = {&b4, &supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S0, NULL};


// states init
const State supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S0 = {false, SUP_DEBUG_STR("S0_S0_S0_S0"), &supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S1 = {false, SUP_DEBUG_STR("S0_S0_S0_S1"), &supR7Mesa_GiratoriaTesteRobo_S0_S0_S0_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S0 = {false, SUP_DEBUG_STR("S0_S1_S0_S0"), &supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S1 = {false, SUP_DEBUG_STR("S0_S1_S0_S1"), &supR7Mesa_GiratoriaTesteRobo_S0_S1_S0_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S0 = {false, SUP_DEBUG_STR("S1_S0_S0_S0"), &supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S1 = {false, SUP_DEBUG_STR("S1_S0_S0_S1"), &supR7Mesa_GiratoriaTesteRobo_S1_S0_S0_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0 = {false, SUP_DEBUG_STR("S1_S0_S1_S0"), &supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S1 = {false, SUP_DEBUG_STR("S1_S0_S1_S1"), &supR7Mesa_GiratoriaTesteRobo_S1_S0_S1_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0 = {false, SUP_DEBUG_STR("S1_S1_S0_S0"), &supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1 = {false, SUP_DEBUG_STR("S1_S1_S0_S1"), &supR7Mesa_GiratoriaTesteRobo_S1_S1_S0_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0 = {false, SUP_DEBUG_STR("S1_S1_S1_S0"), &supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1 = {false, SUP_DEBUG_STR("S1_S1_S1_S1"), &supR7Mesa_GiratoriaTesteRobo_S1_S1_S1_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0 = {true, SUP_DEBUG_STR("S6_S0_S0_S0"), &supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1 = {false, SUP_DEBUG_STR("S6_S0_S0_S1"), &supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0 = {false, SUP_DEBUG_STR("S6_S0_S1_S0"), &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1 = {false, SUP_DEBUG_STR("S6_S0_S1_S1"), &supR7Mesa_GiratoriaTesteRobo_S6_S0_S1_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S0 = {false, SUP_DEBUG_STR("S6_S1_S0_S0"), &supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1 = {false, SUP_DEBUG_STR("S6_S1_S0_S1"), &supR7Mesa_GiratoriaTesteRobo_S6_S1_S0_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0 = {false, SUP_DEBUG_STR("S6_S1_S1_S0"), &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1 = {false, SUP_DEBUG_STR("S6_S1_S1_S1"), &supR7Mesa_GiratoriaTesteRobo_S6_S1_S1_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S0 = {false, SUP_DEBUG_STR("S7_S0_S0_S0"), &supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1 = {false, SUP_DEBUG_STR("S7_S0_S0_S1"), &supR7Mesa_GiratoriaTesteRobo_S7_S0_S0_S1_t0};
const State supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S0 = {false, SUP_DEBUG_STR("S7_S1_S0_S0"), &supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S0_t0};
const State supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S1 = {false, SUP_DEBUG_STR("S7_S1_S0_S1"), &supR7Mesa_GiratoriaTesteRobo_S7_S1_S0_S1_t0};

// Supervisor create
Supervisor supR7Mesa_GiratoriaTesteRobo = {&supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0, &supR7Mesa_GiratoriaTesteRobo_S6_S0_S0_S0, NULL,  &supR7Mesa_GiratoriaTesteRobo_a4_evt0, "supR7Mesa_GiratoriaTesteRobo"};
