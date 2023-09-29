import math
from formas.forma import Forma
from colores.color import Color

class Circulo(Forma):

    def __init__(self, color: Color, diametro: float):
        super().__init__(color)
        self.nombre = 'Circulo'
        self._diametro = diametro
        self._radio = diametro / 2

    def getRadio(self) -> float:
        return 2 * math.pi * self._radio
    
    def getArea(self) -> float:
        return math.pi * (self._radio ** 2)