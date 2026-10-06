# patrones_de_diseño/estructurales/bridge/abstraccion/cuadrado.py
from implementacion.renderizador import Renderizador
from abstraccion.forma import Forma

class Cuadrado(Forma):
    def __init__(self, lado: float, renderizador: Renderizador):
        super().__init__(renderizador)
        self.lado = lado
        
        
    def dibujar(self) -> str:
        # Delega el trabajo a través del puente
        return self._renderizador.dibujar_circulo(self.lado)