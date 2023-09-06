import fabricas_concretas as fc

def codigo():
    while True:
      tipoEntrega = int(input('Que tipo de entrega desea tomar: (0=Salir, 1=Terrestre, 2=Maritimo, 3=Aereo):'))
      if tipoEntrega == 1:
          entrega = fc.EntregaTerrestre()
      elif tipoEntrega == 2:
          entrega = fc.EntregaMaritima()
      elif tipoEntrega == 3:
          entrega = fc.EntregaAerea()
      else:
          break
      
      vehiculo = entrega.fabrica()

      vehiculo.carga()
      vehiculo.viaje()
      impuestos = vehiculo.pagoImpuestos()
      vehiculo.entrega()
      print('=== Los impuestos totales son:', impuestos)

codigo()