from fabricas import FabricaModerna, FabricaArtDeco, FabricaVictoriana

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