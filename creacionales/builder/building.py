class Building():

    def __init__(self) -> None:
        self.windows = { 'cantidad': None, 'material': None}
        self.doors = { 'cantidad': None, 'material': None}
        self.walls = { 'cantidad': None, 'material': None}
        self.roof = { 'cantidad': None, 'material': None}
        self.pool = { 'cantidad': None, 'material': None}
    
    def setWindows(self, cantidad: int, material: str):
        self.windows['cantidad'] = cantidad
        self.windows['material'] = material

    def setDoors(self, cantidad: int, material: str):
        self.windows['cantidad'] = cantidad
        self.windows['material'] = material

    def setWalls(self, cantidad: int, material: str):
        self.windows['cantidad'] = cantidad
        self.windows['material'] = material

    def setRoof(self, cantidad: int, material: str):
        self.windows['cantidad'] = cantidad
        self.windows['material'] = material

    def setPool(self, cantidad: int, material: str):
        self.windows['cantidad'] = cantidad
        self.windows['material'] = material