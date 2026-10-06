# patrones_de_diseño/estructurales/bridge/abstraccion/forma.py
from abc import ABC, abstractmethod
from implementacion.renderizador import Renderizador

class Forma(ABC):
    """
    CONCEPTO: "Clase principal... y solo se conectan utilizando una interaz
    como puente".
    
    'self._renderizador' es el PUENTE (Brigde). La clase principal no hereda
    del motor gráfico; lo compone a través de su interfaz.
    """
    def __init__(self, renderizador: Renderizador):
        self._renderizador = renderizador
        
        @abstractmethod
        def dibujar(self) -> str:
            pass
    