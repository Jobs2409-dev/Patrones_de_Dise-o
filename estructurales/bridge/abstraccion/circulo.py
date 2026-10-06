# patrones_de_diseño/estructurales/bridge/abstraccion/circulo.py
from abstraccion.forma import Forma
from implementacion.renderizador import Renderizador

class Circulo(Forma):
    """
    CONCEPTO: "Alteración estructural... sin tener ningún efecto entre ellas".
    
    Podemos crear nuevas formas sin tocar ninguna clase de renderizado.
    """
    def __init__(self, radio: float, renderizador: Renderizador):
        super().__init__(renderizador)
        self.radio = radio
        
    def dibujar(self) -> str:
        # Delega el trabajo a través del puente
        return self._renderizador.dibujar_circulo(self.radio)