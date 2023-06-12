/*
O supervisor será formado por uma matriz em que as linhas representam os estados
e as colunas apontam para a posição na matriz de transições.
A matriz de transições será formada por uma matriz de X linhas e 2 colunas, onde
X é o número de transições possíveis. A primeira coluna apontará para o evento e
a segunda para o estado de destino.
*/
#include "events.h"
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

bool handle_event(uint32_t event);

typedef struct _Supervisor Supervisor;
/**
 * @brief The supervisor
 */
struct _Supervisor {
  uint32_t initial_state;
  uint32_t current_state;
  uint32_t last_state;
  const char *name;
};

// Definição dos estados
#define sup_G1S0_E1S0_E2S0_G2S0 0
#define sup_G1S0_E1S0_E2S0_G2S1 1
#define sup_G1S0_E1S0_E2S1_G2S1 2
#define sup_G1S0_E1S1_E2S0_G2S0 3
#define sup_G1S0_E1S1_E2S0_G2S1 4
#define sup_G1S0_E1S1_E2S1_G2S0 5
#define sup_G1S0_E1S1_E2S1_G2S1 6

// Representa o a quantidade de transições no estado com maior número de
// transições
#define STATE_MAX_TRANSITIONS 2

uint32_t transitions[][2] = {
    {btn, sup_G1S0_E1S1_E2S1_G2S0},     {desliga, sup_G1S0_E1S0_E2S0_G2S0},
    {btn, sup_G1S0_E1S1_E2S1_G2S1},     {btn, sup_G1S0_E1S1_E2S0_G2S1},
    {liga, sup_G1S0_E1S0_E2S0_G2S1},    {btn, sup_G1S0_E1S1_E2S1_G2S0},
    {desliga, sup_G1S0_E1S1_E2S0_G2S0}, {btn, sup_G1S0_E1S1_E2S1_G2S1},
    {liga, sup_G1S0_E1S0_E2S1_G2S1},    {btn, sup_G1S0_E1S1_E2S0_G2S0},
    {btn, sup_G1S0_E1S1_E2S0_G2S1}};

uint32_t supervisorStates[][STATE_MAX_TRANSITIONS] = {
    {0, NULL}, {1, 2}, {3, NULL}, {4, 5}, {6, 7}, {8, 9}, {10, NULL}};

Supervisor sup = {sup_G1S0_E1S0_E2S0_G2S0, sup_G1S0_E1S0_E2S0_G2S0, NULL,
                  "sup"};

/**
 * Iterate over supervisor matrix
 */
bool handle_event(uint32_t event) {
  // Iterate over supervisor matrix
  for (uint32_t i = 0; i < STATE_MAX_TRANSITIONS; i++) {
    if (transitions[supervisorStates[sup.current_state][i]][0] == event) {
      sup.current_state =
          transitions[supervisorStates[sup.current_state][i]][1];
      return true;
    }
  }
}