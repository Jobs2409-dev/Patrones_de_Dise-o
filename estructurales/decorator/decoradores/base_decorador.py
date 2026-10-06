# patrones_de_diseño/estructurales/decorator/decoradores/base_decorador.py
from interfaces.bebida import Bebida

class DecoradorBase(Bebida):
    """
    CONCEPTO: "Clase decorator proporciona capacidades adicionales".
    
    
    Hereda de 'Bebida' para tener su misma interfaz, pero a la vez
    CONTIENE otra 'Bebida' adentro (por composición). Delega por defecto
    en ella.
    """
    def __init__(self, bebida_a_envolver: Bebida):
        # Mantiene la referencia al objeto que está decorando/envolviendo
        self._bebida = bebida_a_envolver
        
    def obtener_costo(self) -> float:
        return self._bebida.obtener_costo()
    
    def obtener_descripcion(self) -> str:
        return self._bebida.obtener_descripcion()
    