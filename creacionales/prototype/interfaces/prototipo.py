# patrones_de_diseño/creacionales/prototype/interfaces/prototipo.py
from abc import ABC, abstractmethod

class Prototipo(ABC):
    """
    CONCEPTO: "Permite copiar objetos existentes sin hacer que su
    código dependa de sus clases".
    
    Establece el contrato formal de clonación. Toda clase concreta que
    herede debe implementar 'clonar()' para encargarse de su propia 
    suplicación 
    """
    @abstractmethod
    def clonar(self):
        # Devuelve una copia independiente de la instancia actual.
        pass