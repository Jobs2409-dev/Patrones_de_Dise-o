# patrones_de_diseño/creacionales/abstract_factory/productos/producto_claro.py
from interfaces.boton import Boton
from interfaces.checkbox import Checkbox

# Familia 1: Productos tema claro
class BotonClaro(Boton):
    def render(self) -> str:
        return "Boton claro con fondo blanco, texto negro y borde gris."
    
class CheckboxClaro(Checkbox):
    def render(self) -> str:
        return "Checkbox claro con casillas blanca con tilde azul."