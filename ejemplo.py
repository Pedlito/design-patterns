from abc import ABC, abstractmethod


class Creador(ABC):
    
    @abstractmethod
    def metodoFabrica(self):
        pass


class Vehiculo(ABC):
    
    @abstractmethod
    def girar(self) -> str:
        pass
    
    @abstractmethod
    def encender(self) -> str:
        pass


class Barco(Vehiculo):
    
    def encender(self):
        print('Encender el barco')
    
    def girar(self):
        print('Girar el barco')

class ViajeMaritimo(Creador):
    
    def metodoFabrica(self) -> Vehiculo:
        return Barco()
  

class Carro(Vehiculo):
    
    def encender(self):
        print('Encender el carro')
    
    def girar(self):
        print('Girar el carro')

class ViajeTerrestre(Creador):
    
    def metodoFabrica(self) -> Vehiculo:
        return Carro()


class Avion(Vehiculo):
    
    def encender(self):
        print('Encender el avion')
    
    def girar(self):
        print('Girar el avion')

class ViajeAereo(Creador):
    
    def metodoFabrica(self) -> Vehiculo:
        return Avion()


def codigoCliente():
    while True:
      tipoViaje = int(input('Que tipo de viaje desea tomar: (0=Salir, 1=Terrestre, 2=Maritimo, 3=Aereo):'))
      if tipoViaje == 1:
          viaje = ViajeTerrestre()
      elif tipoViaje == 2:
          viaje = ViajeMaritimo()
      elif tipoViaje == 3:
          viaje = ViajeAereo()
      else:
          break
      
      vehiculo = viaje.metodoFabrica()

      vehiculo.encender()
      vehiculo.girar()

codigoCliente()