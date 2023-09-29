from formas.forma import Forma
from colores.color import Color

class Cuadrado(Forma):

    def __init__(self, color: Color, medidaLado: float):
        super().__init__(color)
        self.nombre = 'Cuadrado'
        self._lado = medidaLado

    def getRadio(self) -> float:
        return self._lado * 4
    
    def getArea(self) -> float:
        return self._lado ** 2
    