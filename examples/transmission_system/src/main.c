/**
 * @file main.c
 *
 * @brief Main file for the supervisor project
 */
#include "event_handler/event_handler.h"
#include "event_handler/events.h"
#include <stdio.h>
/* ----- Examples for the transmission system --- */
char output_buffer_tran_1[256] = [];
char output_buffer_tran_2[256] = [];

/**
 * Sends the message over the transmission channel
 * The implementation should be done in a separate file
 *
 * @param buffer A pointer to a character array containing the message to be
 * sent.
 * @param transmitter An unsigned 8-bit integer representing the ID or
 * identifier of the transmitter.
 *
 * @return An unsigned 8-bit integer indicating the result of the operation.
 *         Typically, 0 for success or an error code for failure.
 */
uint8_t send_message(char *buffer, uint8_t transmitter);

/**
 * Receives a message from the transmission channel
 * The implementation should be done in a separate file
 *
 * @param buffer A pointer to a character array where the received message will
 * be stored.
 *
 * @param transmitter An unsigned 8-bit integer representing the ID or
 * identifier of the transmitter from which the message will be received.
 *
 * @return An unsigned 8-bit integer indicating the result of the operation.
 *         Typically, 0 for success or an error code for failure.
 */
uint8_t receive_message(char *buffer, uint8_t transmitter);

/* ----- End of examples for the transmission system --- */

/**
 * Action for controllable event tran_1
 */
void tran_1_action(const Event *event) {
  if (send_message(output_buffer_tran_1, 1)) {
    trigger_event(&ack_1); // TODO: This check must be asynchronous
  }
}

/**
 * Action for controllable event tran_2
 */
void tran_2_action(const Event *event) {
  if (send_message(output_buffer_tran_2, 2)) {
    trigger_event(&ack_2); // TODO: This check must be asynchronous
  }
}

void setup(void) {
  // set action on controllable events
  set_event_action(&tran_1, tran_1_action);
  set_event_action(&tran_2, tran_2_action);

  // start the controller
  controller_start();
}

int main(void) {
  setup();
  while (true) {
    if (receive_message(output_buffer_tran_1, 1)) {
      trigger_event(&arr_1);
    }
    if (receive_message(output_buffer_tran_2, 2)) {
      trigger_event(&arr_2);
    }
  }
  return 0;
}
