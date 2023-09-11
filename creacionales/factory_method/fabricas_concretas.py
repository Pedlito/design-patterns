import objetos_abstractos as oa
import productos

class EntregaTerrestre(oa.Creador):
    
    def fabrica(self):
        return productos.Camion()
    
class EntregaMaritima(oa.Creador):
    
    def fabrica(self):
        return productos.Barco()

class EntregaAerea(oa.Creador):
    
    def fabrica(self):
        return productos.Avion()