from abc import ABC, abstractmethod
from objetos_abstractos import Silla, Mesa, Cama

class SillaModerna(Silla):

    estilo = 'Moderna'
    patas = 1
    color = 'Amarillo'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class MesaModerna(Mesa):

    estilo = 'Moderna'
    patas = 3
    color = 'Verde'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class CamaModerna(Cama):

    estilo = 'Moderna'
    patas = 4
    color = 'Blanco'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)