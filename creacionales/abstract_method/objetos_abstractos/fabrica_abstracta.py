from abc import ABC, abstractmethod

class FabricaAbstracta(ABC):
    """Clase abstracta que define el formato de una fabrica."""
    
    @abstractmethod
    def crearSilla(self):
        pass
    
    
    @abstractmethod
    def crearMesa(self):
        pass

    @abstractmethod
    def crearCama(self):
        pass