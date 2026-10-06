# patrones_de_diseño/creacionales/factory_method/creadores/logistica_t
from creadores.logistica_base import Logistica
from interfaces.transporte import Transporte
from producto.camion import Camion

class LogisticaTierra(Logistica):
    """
    CONCEPTO: "Permite que las subclases alteren el tipo de objetos
    que se crearán".
    
    Sobreescriben el FACTPRY METHOD para retornar un Camion.
    """
    def crear_transporte(self) -> Transporte:
        return Camion()
    