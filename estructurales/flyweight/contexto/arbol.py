# patrones_de_diseño/estructurales/flyweigth/contexto/arbol.py
from flyweigths.tipo_arbol import TipoArbol

class Arbol:
    """
    ESTADO EXTRÍNSECO (Contexto único):
    Cada árbol solo almacena su posición particular en el mundo (x, y)
    y una referencia compartida a su 'TipoArbol' (Flyweight).
    """
    def __init__(self, x: int, y: int, tipo: TipoArbol):
        self.x = x
        self.y = y
        self.tipo = tipo # referencia al objeto pesado compartido
        
    
    def dibujar(self) -> None:
        # Pasa sus coordenadas individuales al flyweight compartido
        self.tipo.dibujar(self.x, self.y)
     