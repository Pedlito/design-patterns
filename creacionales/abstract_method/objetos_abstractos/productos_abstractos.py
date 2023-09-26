from abc import ABC, abstractmethod

class Silla(ABC):
    """Clase abstracta que define como es una silla"""

    @abstractmethod
    def mostrarInformacion(self):
        pass


class Mesa(ABC):
    """Clase abstracta que define como es una mesa"""

    @abstractmethod
    def mostrarInformacion(self):
        pass


class Cama(ABC):
    """Clase abstracta que define como es una cama"""

    @abstractmethod
    def mostrarInformacion(self):
        pass