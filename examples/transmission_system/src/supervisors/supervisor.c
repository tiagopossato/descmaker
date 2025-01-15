#include <stdbool.h>
#include <stdlib.h>

#include "../event_handler/events.h"
#include "supervisor.h"

// Supervisor specific instances
// alphabet create
const Alphabet supervisor_arr_1_evt0;
const Alphabet supervisor_arr_2_evt1;
const Alphabet supervisor_tran_1_evt2;
const Alphabet supervisor_tran_2_evt3;
const Alphabet supervisor_ack_2_evt4;
const Alphabet supervisor_ack_1_evt5;

// Alphabet init
const Alphabet supervisor_arr_1_evt0 = {&arr_1, &supervisor_arr_2_evt1};
const Alphabet supervisor_arr_2_evt1 = {&arr_2, &supervisor_tran_1_evt2};
const Alphabet supervisor_tran_1_evt2 = {&tran_1, &supervisor_tran_2_evt3};
const Alphabet supervisor_tran_2_evt3 = {&tran_2, &supervisor_ack_2_evt4};
const Alphabet supervisor_ack_2_evt4 = {&ack_2, &supervisor_ack_1_evt5};
const Alphabet supervisor_ack_1_evt5 = {&ack_1, NULL};

// states create
const State supervisor_q0;
const State supervisor_q1;
const State supervisor_q2;
const State supervisor_q4;
const State supervisor_q5;
const State supervisor_q6;
const State supervisor_q7;
const State supervisor_q8;

// transitions create and init
const Transition supervisor_q0_t0;
const Transition supervisor_q0_t1;
const Transition supervisor_q0_t0 = {&arr_1, &supervisor_q1, &supervisor_q0_t1};
const Transition supervisor_q0_t1 = {&arr_2, &supervisor_q4, NULL};

const Transition supervisor_q1_t0;
const Transition supervisor_q1_t1;
const Transition supervisor_q1_t0 = {&arr_2, &supervisor_q2, &supervisor_q1_t1};
const Transition supervisor_q1_t1 = {&tran_1, &supervisor_q7, NULL};

const Transition supervisor_q2_t0;
const Transition supervisor_q2_t0 = {&tran_1, &supervisor_q8, NULL};

const Transition supervisor_q4_t0;
const Transition supervisor_q4_t1;
const Transition supervisor_q4_t0 = {&arr_1, &supervisor_q2, &supervisor_q4_t1};
const Transition supervisor_q4_t1 = {&tran_2, &supervisor_q6, NULL};

const Transition supervisor_q5_t0;
const Transition supervisor_q5_t0 = {&ack_2, &supervisor_q1, NULL};

const Transition supervisor_q6_t0;
const Transition supervisor_q6_t1;
const Transition supervisor_q6_t0 = {&ack_2, &supervisor_q0, &supervisor_q6_t1};
const Transition supervisor_q6_t1 = {&arr_1, &supervisor_q5, NULL};

const Transition supervisor_q7_t0;
const Transition supervisor_q7_t1;
const Transition supervisor_q7_t0 = {&ack_1, &supervisor_q0, &supervisor_q7_t1};
const Transition supervisor_q7_t1 = {&arr_2, &supervisor_q8, NULL};

const Transition supervisor_q8_t0;
const Transition supervisor_q8_t0 = {&ack_1, &supervisor_q4, NULL};


// states init
const State supervisor_q0 = {true, SUP_DEBUG_STR("q0"), &supervisor_q0_t0};
const State supervisor_q1 = {false, SUP_DEBUG_STR("q1"), &supervisor_q1_t0};
const State supervisor_q2 = {false, SUP_DEBUG_STR("q2"), &supervisor_q2_t0};
const State supervisor_q4 = {false, SUP_DEBUG_STR("q4"), &supervisor_q4_t0};
const State supervisor_q5 = {false, SUP_DEBUG_STR("q5"), &supervisor_q5_t0};
const State supervisor_q6 = {false, SUP_DEBUG_STR("q6"), &supervisor_q6_t0};
const State supervisor_q7 = {false, SUP_DEBUG_STR("q7"), &supervisor_q7_t0};
const State supervisor_q8 = {false, SUP_DEBUG_STR("q8"), &supervisor_q8_t0};

// Supervisor create
Supervisor supervisor = {(State *)&supervisor_q0, (State *)&supervisor_q0, NULL,  &supervisor_arr_1_evt0, "supervisor"};
