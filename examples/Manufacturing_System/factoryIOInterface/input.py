from pymodbus.exceptions import ModbusIOException
from .connection import client, modbus_lock, slave

class Input:
    """
    Classe para representar uma entrada digital do Factory IO
    """
    def __init__(self, name, client, address, slave, lock) -> None:
        """
        Construtor da classe. 
        Inicializa as variáveis da instância 
        """
        self.__name = name
        self.__client = client
        self.__address = address
        self.__slave = slave
        self.__lock = lock
        self.__value = False
        self.__action = None

    def set_callback(self, action):
        """
        Método público para definir uma função 
        que será executada quando o valor da entrada mudar
        """
        self.__action = action

    def read_value(self):
        """
        Método público para ler o valor da entrada
        """
        value = self.__value

        try:
            # Acesso exclusivo ao driver modbus
            with modbus_lock:
                # verifica se o cliente não está conectado
                if not client.is_socket_open():
                    # tenta conectar
                    if not client.connect():
                        # Se não conseguir conectar com o driver modbus, retorna o valor anterior
                        print(f"read_value Input {self.__name}: Error: Can't connect to Modbus Driver")
                        return -1
                res = self.__client.read_discrete_inputs(address=self.__address, count=1, slave=self.__slave)

            # Atualiza o valor da entrada
            value = res.bits[0]
            self.set_value(value)
            # print("read_value Input: Connection time: ", time.time() - init_time)
        except ModbusIOException:
            print("read_value Input: Error: Modbus IO Exception")
            return -1
        except Exception as e:
            print(f"read_value Input {self.__name}: Error: {str(e)}")
            return -1
       
        # Retorna o valor da entrada, para o caso de ter sido chamado externamente
        return self.__value
    
    def set_value(self, value):
        """
        Método público para definir o valor da entrada
        """
        # Se o valor da entrada mudou, chama a função de ação
        if value != self.__value:
            self.__value = value
            # Se a função de ação foi definida, chama a função passando o novo valor como parâmetro
            if self.__action:
                self.__action(self.__value)

    def get_value(self):
        """
        Método público que retorna o último valor lido na entrada pelo timer ou pelo método read_value
        """
        return self.__value
    
# Objetos das entradas digitais
sensor_se = Input(name="Sensor se", client=client, address=0, slave=slave, lock=modbus_lock)
sensor_drill_part_detected = Input(name="Drill part detected", client=client, address=1, slave=slave, lock=modbus_lock)
sensor_tester_part_detected = Input(name="Tester part detected", client=client, address=4, slave=slave, lock=modbus_lock)

def input_read_all_values():
    """
    Função para ler todos os valores das entradas digitais
    E atualizar os valores dos objetos das entradas digitais
    """
    res = []
    try:
        # Tenta conectar com o driver modbus
        # measure connection time
        # init_time = time.time()
        # Acesso exclusivo ao driver modbus
        with modbus_lock:
            # verifica se o cliente não está conectado
            if not client.is_socket_open():
                # tenta conectar
                if not client.connect():
                    # Se não conseguir conectar com o driver modbus, retorna o valor anterior
                    print("read_value Input: Error: Can't connect to Modbus Driver")
                    return -1
            res = client.read_discrete_inputs(address=0, count=3, slave=slave)

        sensor_se.set_value(res.bits[0])
        sensor_drill_part_detected.set_value(res.bits[1])
        sensor_tester_part_detected.set_value(res.bits[2])

    except ModbusIOException:
        print("read_value Input: Error: Modbus IO Exception")
        return -1
    except Exception as e:
        print(f"read_value Input: Error: {str(e)}")
        return -1
  

