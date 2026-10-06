# patrones_de_diseño/creacionales/factory_method/creadores/logistica_aire.py
from interfaces.transporte import Transporte
from creadores.logistica_base import Logistica
from producto.avion import Avion

class LogisticaAire(Logistica):
    
    """
    CONCEPTO: "Permite que las subclases alteren el tipo de objeto que se
    crearán".
    
    Sobreescriben el FACTORY METHOD para retornar un Avión
    """
    def crear_transporte(self) -> Transporte:
        return Avion()