# patrones_de_diseño/estructurales/bridge/implementacion/renderizador.py
from abc import ABC, abstractmethod

class Renderizador(ABC):
    """
    CONCEPTO: "Implementador de interfaces".
    
    Esta interfaz actúa como el externo de la implementacion en el puente.
    Las clases principalkes no concoen los detalles ténicos de esta capa.
    """
    @abstractmethod
    def dibujar_circulo(self, radio: float) -> str:
        pass
    
    @abstractmethod
    def dibujar_cuadrado(self, lado: float) -> str:
        pass