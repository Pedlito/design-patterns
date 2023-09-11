from abc import ABC, abstractmethod
from objetos_abstractos import Silla, Mesa, Cama

class SillaVictoriana(Silla):

    estilo = 'Victoriana'
    patas = 3
    color = 'Veige'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class MesaVictoriana(Mesa):

    estilo = 'Victoriana'
    patas = 1
    color = 'Café'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class CamaVictoriana(Cama):

    estilo = 'Victoriana'
    patas = 9
    color = 'Azul'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)