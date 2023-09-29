from abc import ABC, abstractmethod
from colores.color import Color

class Forma(ABC):
    """
    Clase abstracta que representa la forma de las figuras.
    Todas las formas que se creen deben de implementar esta estructura.
    """

    nombre = ''

    @abstractmethod
    def __init__(self, color: Color):
        """Constructor de la forma, solicita el color y las propiedades necesarias para la forma."""
        self.color = color
        pass

    @abstractmethod
    def getRadio(self) -> float:
        """Obtiene el radio de la forma"""
        pass

    @abstractmethod
    def getArea(self) -> float:
        """Obtiene el área de la forma"""
        pass

    def getColorName(self) -> str:
        """Obtiene el color de la forma"""
        return self.color.getColor()