# patrones_de_diseño/creacionales/abstract_factory/fabrica/fabrica_claro.py
from interfaces.fabrica_gui import FabricaGUI
from interfaces.boton import Boton
from interfaces.checkbox import Checkbox
from productos.producto_claro import BotonClaro, CheckboxClaro


class FabricaTemaClaro(FabricaGUI):
    """
    CONCEPTO: "Garantiza que todos los elementos creados sean del tema claro."
    """
    def crear_boton(self) -> Boton:
        return BotonClaro()
    
    def crear_checkbox(self) -> Checkbox:
        return CheckboxClaro()
    
    
    