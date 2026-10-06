# patrones_de_diseño/creacionales/abstract_factory/fabrica/fabrica_oscuro.py
from interfaces.fabrica_gui import FabricaGUI
from interfaces.boton import Boton
from interfaces.checkbox import Checkbox
from productos.producto_oscuro import BotonOscuro, CheckbosOscuro


class FabricaTemaOscuro(FabricaGUI):
    """
    CONCEPTO: "Garantiza que todos los elementos creados sean del
    oscuro.
    """
    def crear_boton(self) -> Boton:
        return BotonOscuro()
    
    def crear_checkbox(self) -> Checkbox:
        return CheckbosOscuro()
        
    