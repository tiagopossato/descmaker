"""
Arquivo principal do programa. Contém a função main que é executada ao iniciar o programa.
Possui todas as funções de ação para cada evento.
"""
from code_python import Events
from code_python import trigger_event
from threading import Timer
from time import sleep

from factoryIOInterface import *

# Variável global para indicar se a simulação está rodando ou não
run_simulation = True

# Fator de escala para o tempo da simulação
FACTORY_IO_TIME_SCALE = 1

#-------- CAMADA FÍSICA ENTRADAS ----------------
# Define as funções e associa às entradas do CLP
# essas ações são executadas toda vez que o valor da entrada muda
def sensor_se_action(value):
    """
    Ação executada toda vez que o valor da entrada A mudar
    """
    # Verifica se o sensor detectou a caixa
    # print(f'sensor_se {value}')
    if(value == False):
        trigger_event(Events['se'])
# associa a ação ao evento
sensor_se.set_callback(sensor_se_action)

def sensor_drill_part_detected_action(value):
    """
    Ação executada toda vez que o valor mudar
    """
    if(value == True):
        print(f'sensor_drill_part_detected {value}')
        stop_drill()
sensor_drill_part_detected.set_callback(sensor_drill_part_detected_action)

def sensor_tester_part_detected_action(value):
    """
    Ação executada toda vez que o valor mudar
    """
    if(value == True):
        print(f'sensor_tester_part_detected {value}')
        stop_tester()
sensor_tester_part_detected.set_callback(sensor_tester_part_detected_action)


#-------- FIM DA CAMADA FÍSICA ENTRADAS ----------------

def motor_a1_action(event):
    """
    Função para ligar o motor da esteira A
    Evento controlável a0
    """
    motor_a1.on()
    if run_simulation == False:
        return
    # inicia um timer para ligar o motor da esteira D que retira a caixa da esteira A
    Timer(1.5/FACTORY_IO_TIME_SCALE, motor_b1_action).start()

def motor_b1_action():
    motor_a1.off()
    trigger_event(Events['b1'])

def motor_a0_action(event):
    """
    Função para ligar o motor da esteira A
    Evento controlável a0
    """
    # print('Ligando mesa')
    for motor in motor_a0:
        motor.on()
    if run_simulation == False:
        return
    # inicia um timer para ligar o motor da esteira D que retira a caixa da esteira A
    Timer(3.25/FACTORY_IO_TIME_SCALE, motor_b0_action).start()

def motor_b0_action():
    for motor in motor_a0:
        motor.off()
    trigger_event(Events['b0'])

def start_drill(event):
    start_drill_a2.on()
    if run_simulation == False:
        return

def stop_drill():
    start_drill_a2.off()
    trigger_event(Events['b2'])

def start_tester(event):
    start_tester_a3.on()
    if run_simulation == False:
        return

def stop_tester():
    start_tester_a3.off()
    trigger_event(Events['b3'])


# -------- 'ROBOT' -------------
def start_arm(event):
    start_arm_a4.on()
    Timer(2.25/FACTORY_IO_TIME_SCALE,stop_arm).start()

def stop_arm():
    start_arm_a4.off()
    trigger_event(Events['b4'])
# -------- 'ROBOT' -----------
    
Events['a0'].set_action(motor_a0_action)
Events['a1'].set_action(motor_a1_action)
Events['a2'].set_action(start_drill)
Events['a3'].set_action(start_tester)
Events['a4'].set_action(start_arm)

if __name__ == '__main__':
    factory_io_reset.on()
    factory_io_reset.off()
    factory_io_run.on()
    while True:
        try:
            input_read_all_values()
            sleep(.01)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:            
            run_simulation  = False
            factory_io_pause.on()
            print("Interrompendo a simulação, aguarde o encerramento...")
            break
