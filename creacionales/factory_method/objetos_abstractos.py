import time
import abc

esperaCorta: int = 1
esperaNormal: int = 2
esperaLarga: int = 3

class Creador(abc.ABC):
    
    @abc.abstractmethod
    def fabrica(self):
        pass

class Transporte(abc.ABC):
     
    # @abc.abstractmethod
    def carga(self):
        print('=== Cargando mercaderia en central de abasto...')
        time.sleep(esperaNormal)
        print('\tCarga realizada con exito\n')

    
    @abc.abstractmethod
    def viaje(self):
        pass
    
    @abc.abstractmethod
    def pagoImpuestos(self):
        pass
    
    # @abstractmethod
    def entrega(self):
        print('=== Entregando mercadería...')
        time.sleep(esperaNormal)
        print('\tEntrega realizada con exito\n')