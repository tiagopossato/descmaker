"""
Arquivo para conexão com o driver modbus
"""
import configparser
import os
from pymodbus.client import ModbusTcpClient
from threading import Lock

# Lê as configurações do arquivo config.ini
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# Cria o cliente modbus
client = ModbusTcpClient(config['modbus']['host'], port=int(config['modbus']['port']))

# Endereço do escravo
slave = int(config['modbus']['slave'])

# Semáforo para acesso único ao driver modbus
# Dessa forma é garantido que, quando uma requisição for feita,
# ela será concluída antes de outra requisição ser feita
modbus_lock = Lock()
