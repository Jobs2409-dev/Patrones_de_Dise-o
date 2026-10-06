# patrones_de_diseño/estructurales/flyweigth/contexto/bosque.py
from flyweigths.arbol_factory import ArbolFactory
from contexto.arbol import Arbol

class Bosque:
    """
    Colección masiva de árboles.
    """
    def __init__(self):
        self._arboles: list[Arbol] = []
        
    def plantar_arbol(self, x: int, y: int, especie: str, color: str, textura: str) -> None:
        # Pide a la fábrica el tipo reutilizable
        tipo = ArbolFactory.obtener_tipo_arbol(especie, color, textura)
        arbol = Arbol(x, y, tipo)
        self._arboles.append(arbol)
        
    def renderizar(self) -> None:
        for arbol in self._arboles:
            arbol.dibujar()
            
    def cantidad_arboles(self) -> int:
        return len(self._arboles)
    