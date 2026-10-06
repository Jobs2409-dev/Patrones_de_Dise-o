# patrones_de_diseño/creacionales/abstract_factory/productos/producto_oscuro.py
from interfaces.boton import Boton
from interfaces.checkbox import Checkbox

# Familia 2: Productos tema oscuro
class BotonOscuro(Boton):
    def render(self) -> str:
        return "Boton oscuro con fondo gris, txt blanco y sin bordes."
    
class CheckbosOscuro(Checkbox):
    def render(self) -> str:
        return "Checkbox oscuro, casillas negras con tilde verde neón."