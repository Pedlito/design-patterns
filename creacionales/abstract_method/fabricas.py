from objetos_abstractos import FabricaAbstracta, Silla, Mesa, Cama
import productos

class FabricaModerna(FabricaAbstracta):
    """Fabrica para productos Modernos"""

    def crearSilla(self) -> Silla:
        return productos.SillaModerna()
    
    def crearMesa(self) -> Mesa:
        return productos.MesaModerna()
    
    def crearCama(self) -> Cama:
        return productos.CamaModerna()
    
class FabricaVictoriana(FabricaAbstracta):
    """Fabrica para productos Victorianos"""

    def crearSilla(self) -> Silla:
        return productos.SillaVictoriana()
    
    def crearMesa(self) -> Mesa:
        return productos.MesaVictoriana()
    
    def crearCama(self) -> Cama:
        return productos.CamaVictoriana()
    
class FabricaArtDeco(FabricaAbstracta):
    """Fabrica para productos ArtDeco"""

    def crearSilla(self) -> Silla:
        return productos.SillaArtDeco()
    
    def crearMesa(self) -> Mesa:
        return productos.MesaArtDeco()
    
    def crearCama(self) -> Cama:
        return productos.CamaArtDeco()