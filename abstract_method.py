from abc import ABC, abstractmethod


# Fabrica abstracta
class FabricaAbstracta(ABC):
    
    @abstractmethod
    def crearSilla(self):
        pass
    
    
    @abstractmethod
    def crearMesa(self):
        pass

    @abstractmethod
    def crearCama(self):
        pass

# Productos abstractos
class Silla(ABC):

    @abstractmethod
    def mostrarInformacion(self):
        pass


class Mesa(ABC):

    @abstractmethod
    def mostrarInformacion(self):
        pass


class Cama(ABC):

    @abstractmethod
    def mostrarInformacion(self):
        pass


# Productos
class SillaModerna(Silla):

    estilo = 'Moderna'
    patas = 1
    color = 'Amarillo'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class SillaVictoriana(Silla):

    estilo = 'Victoriana'
    patas = 3
    color = 'Veige'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class SillaArtDeco(Silla):

    estilo = 'ArtDeco'
    patas = 4
    color = 'Café'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class MesaModerna(Mesa):

    estilo = 'Moderna'
    patas = 3
    color = 'Verde'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class MesaVictoriana(Mesa):

    estilo = 'Victoriana'
    patas = 1
    color = 'Café'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class MesaArtDeco(Mesa):

    estilo = 'ArtDeco'
    patas = 4
    color = 'Amarillo'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class CamaModerna(Cama):

    estilo = 'Moderna'
    patas = 4
    color = 'Blanco'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class CamaVictoriana(Cama):

    estilo = 'Victoriana'
    patas = 9
    color = 'Azul'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

class CamaArtDeco(Cama):

    estilo = 'ArtDeco'
    patas = 4
    color = 'Blanco'

    def mostrarInformacion(self):
        print('Información:\n\tEstilo:', self.estilo, '\n\tColor:', self.color, '\n\tPatas:', self.patas)

# Fabricas
class FabricaModerna(FabricaAbstracta):

    def crearSilla(self) -> Silla:
        return SillaModerna()
    
    def crearMesa(self) -> Mesa:
        return MesaModerna()
    
    def crearCama(self) -> Cama:
        return CamaModerna()
    
class FabricaVictoriana(FabricaAbstracta):

    def crearSilla(self) -> Silla:
        return SillaVictoriana()
    
    def crearMesa(self) -> Mesa:
        return MesaVictoriana()
    
    def crearCama(self) -> Cama:
        return CamaVictoriana()
    
class FabricaArtDeco(FabricaAbstracta):

    def crearSilla(self) -> Silla:
        return SillaArtDeco()
    
    def crearMesa(self) -> Mesa:
        return MesaArtDeco()
    
    def crearCama(self) -> Cama:
        return CamaArtDeco()


def code():
    salir = True
    while salir:
        estilo: int = int(input('Que estilo desea ver? (0=salir, 1=Victoriana, 2=ArtDeco, 3=Moderna) '))
        
        if estilo == 1:
            fabrica = FabricaVictoriana()
        elif estilo == 2:
            fabrica = FabricaArtDeco()
        elif estilo == 3:
            fabrica = FabricaModerna()
        else:
            salir = False
            continue

        regresar = False
        while not regresar:
            tipoProducto: int = int(input('Que producto desea ver? (0=Regresar, 1=Sillas, 2=Mesas, 3=Camas) '))

            if tipoProducto == 1:
                producto = fabrica.crearSilla()
            elif tipoProducto == 2:
                producto = fabrica.crearMesa()
            elif tipoProducto == 3:
                producto = fabrica.crearCama()
            else:
                regresar = True
                continue

            producto.mostrarInformacion()

code()