# patrones_de_diseño/estructurales/decorator/interfaces/bebida.py
from abc import ABC, abstractmethod


class Bebida(ABC):
    """
    CONCEPTO: "Restringe la alteración de la estructura del objeto".
    
    Interfaz común. Garantiza que cualquier café o agregado respete
    los mismos métodos de costo y descripción.
    """
    @abstractmethod
    def obtener_costo(self) -> float:
        pass
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass