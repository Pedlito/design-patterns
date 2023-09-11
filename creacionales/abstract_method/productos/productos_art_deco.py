from abc import ABC, abstractmethod
from objetos_abstractos import Silla, Mesa, Cama

class SillaArtDeco(Silla):

    estilo = 'ArtDeco'
    patas = 4
    color = 'Café'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class MesaArtDeco(Mesa):

    estilo = 'ArtDeco'
    patas = 4
    color = 'Amarillo'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class CamaArtDeco(Cama):

    estilo = 'ArtDeco'
    patas = 4
    color = 'Blanco'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)