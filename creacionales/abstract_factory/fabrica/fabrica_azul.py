# patrones_de_diseño/creacionales/abstract_factory/fabrica/fabrica_azul.py
from interfaces.fabrica_gui import FabricaGUI
from interfaces.boton import Boton
from interfaces.checkbox import Checkbox
from productos.producto_azul import BotonAzul, CheckboxAzul

class FabricaTemaAzul(FabricaGUI):
    """
    CONCEPTO: "Garantiza que todos los elementos sean del tema azul."
    """
    def crear_boton(self) -> Boton:
        return BotonAzul()
    
    def crear_checkbox(self) -> Checkbox:
        return CheckboxAzul()
     