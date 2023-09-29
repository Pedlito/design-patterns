import sys

from formas.cuadrado import Cuadrado
from formas.circulo import Circulo
from formas.triangulo import Triangulo
from colores.rojo import Rojo
from colores.base import Base
from colores.azul import Azul

def codigoCliente():
    continuar = True
    while continuar:
        seleccionForma: int = int(input('¿Que forma desea utilizar? (0=salir, 1=Cuadrado, 2=Circulo, 3=Triangulo) '))

        if seleccionForma == 0:
            continuar = False
            continue

        seleccionColor: int = int(input('¿De que color desea pintar la forma seleccionada? (0=cancelar, 1=No pintar, 2=Rojo, 3=Azul) '))
        if seleccionColor == 0:
            continue

        color = Base()
        if seleccionColor == 2:
            color = Rojo()
        elif seleccionColor == 3:
            color = Azul()

        if seleccionForma == 1:
            lado: float = float(input('Ingrese la medida de unos de los lados del cuadrado: '))
            forma = Cuadrado(color, lado)
        elif seleccionForma == 2:
            diametro: float = float(input('Ingrese el diametro del circulo: '))
            forma = Circulo(color, diametro)
        elif seleccionForma == 3:
            lado: float = float(input('Ingrese la medida de uno de los lados del triangulo: '))
            forma = Triangulo(color, lado)
        
        print('=== Salida ===')
        print('\tForma:', forma.nombre)
        print('\tColor:', forma.getColorName())
        print('\tRadio:', forma.getRadio())
        print('\tArea:', forma.getArea(), '\n')

codigoCliente()