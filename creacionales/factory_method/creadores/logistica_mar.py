# patrones_de_diseño/creacionales/factory_method/creadores/logistica_mar.py
from creadores.logistica_base import Logistica
from interfaces.transporte import Transporte
from producto.barco import Barco

class LogisticaMar(Logistica):
    
    """
    CONCEPTO: "Permite que las subclases alteren el tipo de objetos
    que se crearán".
    
    Sobreescriben el FACTORY METHOD para retornar un Barco
    """
    def crear_transporte(self) -> Transporte:
        return Barco()