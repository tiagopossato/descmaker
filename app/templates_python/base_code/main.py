"""
Arquivo principal do projeto. 
É substituído pelo maker.py na hora de converter o supervisor.
"""
from Supervisor import Events, Event, trigger_event
from time import sleep
# install getkey with: pip install getkey
from getkey import getkey

def liga_action(event: Event):
    print('\n\nLigando...\n')

def desliga_action(event: Event):
    print('\n\nDesligando...\n')

# set default action for example
Events['liga'].set_action(liga_action)
Events['desliga'].set_action(desliga_action)

if __name__ == '__main__':
    # handle events for teste
    while True:
        print('Pressione "b" para ligar/desligar ou "q" para sair')
        # read one char from stdin
        key = getkey()
        if key == 'b':
            trigger_event(Events['btn'])
        if key == 'q':
            break
