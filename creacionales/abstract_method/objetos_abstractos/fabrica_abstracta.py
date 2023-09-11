from abc import ABC, abstractmethod

class FabricaAbstracta(ABC):
    
    @abstractmethod
    def crearSilla(self):
        pass
    
    
    @abstractmethod
    def crearMesa(self):
        pass

    @abstractmethod
    def crearCama(self):
        pass