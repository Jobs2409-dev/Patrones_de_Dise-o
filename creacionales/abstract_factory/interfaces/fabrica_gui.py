# patrones_de_diseño/creacionales/abstract_factory/interfaces_productos/fabrica_gui.py
from abc import ABC, abstractmethod
from interfaces.boton import Boton
from interfaces.checkbox import Checkbox

"""
CONCEPTO: "Una interfaz crea un conjunto o familias de objetos 
relacionados"

Define la fábrica abstracta. No implementa la creación directa ni 
especifíca nombres de clases concretas: solo declara los métodos
obligatorios para producir la suite completa de la familia (Botón + Checkbox)
"""
class FabricaGUI(ABC):
    @abstractmethod
    def crear_boton(self) -> Boton:
        # Crea un botón compatible con la familia.
        pass
    
    @abstractmethod
    def crear_checkbox(self) -> Checkbox:
        # Crea un checkbox compatible con la familia.
        pass
    
    

