from abc import ABC, abstractmethod
from objetos_abstractos import Silla, Mesa, Cama

class SillaArtDeco(Silla):
    """Clase que hereda de Silla y define como es una silla ArtDeco"""

    estilo = 'ArtDeco'
    patas = 4
    color = 'Café'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class MesaArtDeco(Mesa):
    """Clase que hereda de Mesa y define como es una mesa ArtDeco"""

    estilo = 'ArtDeco'
    patas = 4
    color = 'Amarillo'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class CamaArtDeco(Cama):
    """Clase que hereda de Cama y define como es una cama ArtDeco"""

    estilo = 'ArtDeco'
    patas = 4
    color = 'Blanco'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)