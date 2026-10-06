# patrones_de_diseño/creacionales/factory_method/interfaces/transporte.py
from abc import ABC, abstractmethod

class Transporte(ABC):
    """
    CONCEPTO: "Interfaces comunes"
    
    Define el contacto formal para todos los productos creados por la
    fabrica. La superclase creadora y el cliente solo dependerán de esta
    abstracción.
    """
    @abstractmethod
    def entregar(self) -> str:
        # Realiza la acción concreta de la entrega.
        pass