# patrones_de_diseño/creacionales/abstract_factory/interfaces_productos/boton.py
from abc import ABC, abstractmethod


"""
CONCEPTO: "El objeto relacionados" 

Cada elemento de la UI debe cumplir un contrato.
Esta interfaz define qué método DEBEN existir para cualquier botón,
permitiendo al cliente interactuar con él sin conocer la clase concreta.
"""
class Boton(ABC):
    # Responsabilidad única: define el contrato formal exclusivo para
    # los objetos de tipo Botón.
    def render(self) -> str: 
        # Dibuja el botón en pantalla
        pass