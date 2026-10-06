# patrones_de_diseño/creacionales/abstract_factory/productos/producto_azul.py
from interfaces.boton import Boton
from interfaces.checkbox import Checkbox

# Familia 3: Productos tema azul
class BotonAzul(Boton):
    def render(self) -> str:
        return "Boton azul, txt blanco y esquinas redondeadas."
    
    
class CheckboxAzul(Checkbox):
    def render(self) -> str:
        return "Checkbox azul, casillas celestes con tilde blanco."