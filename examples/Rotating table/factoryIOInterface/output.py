from pymodbus.exceptions import ModbusIOException
from .connection import client, modbus_lock, slave

class Output:
    """
    Classe para representar uma saída digital do Factory IO
    """
    def __init__(self, name, client, address, slave, lock) -> None:
        """
        Construtor da classe.
        Inicializa as variáveis da instância e
        desliga a saída
        """
        self.__name = name
        self.__client = client
        self.__address = address
        self.__slave = slave
        self.__lock = lock
        self.__value = False
        self.off()

    def get_value(self):
        """
        Método público que retorna o valor da saída
        """
        # Acesso exclusivo ao driver modbus
        
        try:
            # Tenta conectar com o driver modbus
            with self.__lock:
                # verifica se o cliente não está conectado
                if not self.__client.is_socket_open():
                    # tenta conectar
                    if not self.__client.connect():
                        # Se não conseguir conectar com o driver modbus, retorna o valor anterior
                        print(f"get_value Output {self.__name}: Error: Can't connect to Modbus Driver")
                        return -1
                # Lê o valor da saída
                res = self.__client.read_coils(address=self.__address, count=1, slave=self.__slave)

        except ModbusIOException as e:
            print(f"get_value Output: Error {self.__name}: Modbus IO Exception: {str(e)}")
            return -1
        except Exception as e:
            print(f"get_value Output {self.__name}: Error: {str(e)}")
            return -1
        # Atualiza o valor da saída
        self.__value = res.bits[0]
        # Retorna o valor da saída
        return self.__value
            
    def set_vale(self, value):
        """
        Método público que escreve o valor na saída
        """
        try:
            # Acesso exclusivo ao driver modbus
            with self.__lock:
                # verifica se o cliente não está conectado
                if not self.__client.is_socket_open():
                    # tenta conectar
                    if not self.__client.connect():
                        # Se não conseguir conectar com o driver modbus, retorna o valor anterior
                        print(f"set_vale Output {self.__name}: Error: Can't connect to Modbus Driver")
                        return -1
                # Escreve o valor na saída
                self.__client.write_coil(address=self.__address, value=value, slave=self.__slave)

        except ModbusIOException:
            print(f"set_vale Output {self.__name}: Error: Modbus IO Exception")
            return -1
        # Uma vez que o protoloco Modbus não responde a escrita,
        # é preciso ler o valor da saída para verificar se o valor foi escrito
        return self.get_value()

    def on(self):
        """
        Método público que liga a saída
        """
        return self.set_vale(True)
    
    def off(self):
        """
        Método público que desliga a saída
        """
        return self.set_vale(False)
    
#  Objetos das saídas digitais
motor_a1 = Output(name="Belt 0", client=client, address = 0, slave=slave, lock=modbus_lock)
motor_a0 = []
motor_a0.append(Output(name="Belt 1", client=client, address = 1, slave=slave, lock=modbus_lock))
motor_a0.append(Output(name="Curved Belt 1", client=client, address = 2, slave=slave, lock=modbus_lock))
motor_a0.append(Output(name="Belt 2", client=client, address = 3, slave=slave, lock=modbus_lock))
motor_a0.append(Output(name="Curved Belt 2", client=client, address = 4, slave=slave, lock=modbus_lock))

start_drill_a2 = Output(name="Drill", client=client, address = 5, slave=slave, lock=modbus_lock)
start_tester_a3 = Output(name="Tester", client=client, address = 6, slave=slave, lock=modbus_lock)
start_arm_a4 = Output(name="Arm Z", client=client, address = 7, slave=slave, lock=modbus_lock)

factory_io_run = Output(name="FACTORY I/O (Run)", client=client, address=8, slave=slave, lock=modbus_lock)
factory_io_pause = Output(name="FACTORY I/O (Pause)", client=client, address=9, slave=slave, lock=modbus_lock)
factory_io_reset = Output(name="FACTORY I/O (Reset)", client=client, address=10, slave=slave, lock=modbus_lock)
