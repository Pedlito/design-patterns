from abc import ABC, abstractmethod

class Color(ABC):
    """Clase abstracta que representan el color que se aplica a la forma."""

    nombre = ''

    @abstractmethod
    def __init__(self):
        """Constructor del color, solicita la información necesaria."""
        pass

    def getColor(self):
        return self.nombre