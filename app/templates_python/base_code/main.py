"""
Arquivo principal do projeto. 
É substituído pelo maker.py na hora de converter o supervisor.
"""
# install getkey with: pip install getkey
from getkey import getkey
from Supervisor import Events, Event, trigger_event, controller_start

def liga_action(event: Event):
    print('\n\nLigando...\n')

def desliga_action(event: Event):
    print('\n\nDesligando...\n')

if __name__ == '__main__':
    # set default action for example
    Events['liga'].set_action(liga_action)
    Events['desliga'].set_action(desliga_action)

    # handle events for teste
    controller_start()
    
    while True:
        print('Pressione "b" para ligar/desligar ou "q" para sair')
        # read one char from stdin
        key = getkey()
        if key == 'b':
            trigger_event(Events['btn'])
        if key == 'q':
            break
