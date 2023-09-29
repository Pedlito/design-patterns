import math
from formas.forma import Forma
from colores.color import Color

class Triangulo(Forma):

    def __init__(self, color: Color, medidaLado: float):
        super().__init__(color)
        self.nombre = 'Triangulo'
        self._lado = medidaLado

    def getRadio(self) -> float:
        return self._lado * 3
    
    def getArea(self) -> float:
        altura = (math.sqrt(3) * self._lado) / 2
        return (self._lado * altura) / 2
    