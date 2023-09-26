from abc import ABC, abstractmethod
from objetos_abstractos import Silla, Mesa, Cama

class SillaVictoriana(Silla):
    """Clase que hereda de Silla y define como es una silla Victoriana"""

    estilo = 'Victoriana'
    patas = 3
    color = 'Veige'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class MesaVictoriana(Mesa):
    """Clase que hereda de Mesa y define como es una mesa Victoriana"""

    estilo = 'Victoriana'
    patas = 1
    color = 'Café'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class CamaVictoriana(Cama):
    """Clase que hereda de Cama y define como es una cama Victoriana"""

    estilo = 'Victoriana'
    patas = 9
    color = 'Azul'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)