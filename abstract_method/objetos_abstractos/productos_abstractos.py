from abc import ABC, abstractmethod

class Silla(ABC):

    @abstractmethod
    def mostrarInformacion(self):
        pass


class Mesa(ABC):

    @abstractmethod
    def mostrarInformacion(self):
        pass


class Cama(ABC):

    @abstractmethod
    def mostrarInformacion(self):
        pass