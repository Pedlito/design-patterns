from .ibuilder import IBuilder
from building import Building

class CastleBuilder(IBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Building()
    
    @property
    def building(self) -> Building:
        product = self._product
        self.reset()
        return product
    
    def setWindows(self, cantidad: int):
        self.windows['cantidad'] = cantidad
        self.windows['material'] = 'Piedra'

    def setDoors(self, cantidad: int):
        self.windows['cantidad'] = cantidad
        self.windows['material'] = 'Piedra'

    def setWalls(self, cantidad: int):
        self.windows['cantidad'] = cantidad
        self.windows['material'] = 'Piedra'

    def setRoof(self, cantidad: int):
        self.windows['cantidad'] = cantidad
        self.windows['material'] = 'Piedra'

    def setPool(self, cantidad: int):
        self.windows['cantidad'] = cantidad
        self.windows['material'] = 'Piedra'