import time
import objetos_abstractos as oa

esperaCorta: int = 1
esperaNormal: int = 2
esperaLarga: int = 3

class Camion(oa.Transporte):
    
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


class Barco(oa.Transporte):
    
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


class Avion(oa.Transporte):
    
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