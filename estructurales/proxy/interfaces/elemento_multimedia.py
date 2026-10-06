# patrones_de_diseño/estructurales/proxy/interfaces/elemento_multimedia.py
from abc import ABC, abstractmethod

class ElementoMultimedia(ABC):
    """
    CONCEPTO: "La interfaz se utiliza para acceder a estas funcionalidades".
    
    Interfaz común (Subject). Garantiza que el cliente pueda tratar al 
    objeto real y al proxy exactamente de la misma manera.
    """
    @abstractmethod
    def mostrar(self) -> None:
        # Acción principal que ejecuta o delega el elemento.
        pass
    