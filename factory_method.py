import time
from abc import ABC, abstractmethod

esperaCorta: int = 1
esperaNormal: int = 2
esperaLarga: int = 3

# interfaces creadora y de trasnporte
class Creador(ABC):
    
    @abstractmethod
    def fabrica(self):
        pass

class Transporte(ABC):
     
    # @abstractmethod
    def carga(self):
        print('=== Cargando mercaderia en central de abasto...')
        time.sleep(esperaNormal)
        print('\tCarga realizada con exito\n')

    
    @abstractmethod
    def viaje(self):
        pass
    
    @abstractmethod
    def pagoImpuestos(self):
        pass
    
    # @abstractmethod
    def entrega(self):
        print('=== Entregando mercadería...')
        time.sleep(esperaNormal)
        print('\tEntrega realizada con exito\n')


# productos
class Camion(Transporte):
    
    def viaje(self):
        print('=== Iniciando viaje...')
        print('\tRevisión de camión')
        time.sleep(esperaCorta)
        print('\tViajando...')
        time.sleep(esperaNormal)
        print('\tSe ha llegado al destino\n')

    def pagoImpuestos(self):
        return 10
    
    def entrega(self):
        print('=== Proceso de entrega...')
        print('\tEntrega directa con cliente')


class Barco(Transporte):
    
    def carga(self):
        print('=== Cargando mercaderia...')
        print('\tLlevando mercadería a puerto...')
        time.sleep(esperaNormal)
        print('\tCargando al barco...')
        time.sleep(esperaCorta)
        print('\tCarga realizada con exito\n')
    
    def viaje(self):
        print('=== Iniciando viaje...')
        print('\tRevisión del barco')
        time.sleep(esperaCorta)
        print('\tValidando clima...')
        time.sleep(esperaCorta)
        print('\tViaje...')
        time.sleep(esperaLarga)
        print('\tSe ha llegado al destino\n')

    def pagoImpuestos(self):
        return 5
    
    # def entrega(self):
    #     print('entrega del barco')


class Avion(Transporte):
    
    def carga(self):
        print('=== Cargando mercaderia...')
        print('\tLlevando mercadería al aeropuerto...')
        time.sleep(esperaLarga)
        print('\tCargando al avion...')
        time.sleep(esperaCorta)
        print('\tCarga realizada con exito\n')
    
    def viaje(self):
        print('=== Iniciando viaje...')
        print('\tRevisión del avion')
        time.sleep(esperaCorta)
        print('\tValidando clima...')
        time.sleep(esperaCorta)
        print('\tViaje...')
        time.sleep(esperaCorta)
        print('\tSe ha llegado al aeropuerto destino\n')

    def pagoImpuestos(self):
        return 20
    
    def entrega(self):
        print('=== Entregando...')
        print('\tJuntando mercadería en aeropuerto')
        time.sleep(esperaCorta)
        print('\tLlevando a punto de entrega')
        time.sleep(esperaCorta)
        print('\tEntrega realizada con exito\n')


# Creadores concretos
class EntregaTerrestre(Creador):
    
    def fabrica(self):
        return Camion()
    
class EntregaMaritima(Creador):
    
    def fabrica(self):
        return Barco()

class EntregaAerea(Creador):
    
    def fabrica(self):
        return Avion()


def codigo():
    while True:
      tipoEntrega = int(input('Que tipo de entrega desea tomar: (0=Salir, 1=Terrestre, 2=Maritimo, 3=Aereo):'))
      if tipoEntrega == 1:
          entrega = EntregaTerrestre()
      elif tipoEntrega == 2:
          entrega = EntregaMaritima()
      elif tipoEntrega == 3:
          entrega = EntregaAerea()
      else:
          break
      
      vehiculo = entrega.fabrica()

      vehiculo.carga()
      vehiculo.viaje()
      impuestos = vehiculo.pagoImpuestos()
      vehiculo.entrega()
      print('=== Los impuestos totales son:', impuestos)

codigo()