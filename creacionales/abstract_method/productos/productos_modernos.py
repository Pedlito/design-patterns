from abc import ABC, abstractmethod
from objetos_abstractos import Silla, Mesa, Cama

class SillaModerna(Silla):
    """Clase que hereda de Silla y define como es una silla Moderna"""

    estilo = 'Moderna'
    patas = 1
    color = 'Amarillo'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class MesaModerna(Mesa):
    """Clase que hereda de Mesa y define como es una mesa Moderna"""

    estilo = 'Moderna'
    patas = 3
    color = 'Verde'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class CamaModerna(Cama):
    """Clase que hereda de Cama y define como es una cama Moderna"""

    estilo = 'Moderna'
    patas = 4
    color = 'Blanco'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)