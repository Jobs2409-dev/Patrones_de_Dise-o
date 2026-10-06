# patrones_de_diseño/estructurales/bridge/implementacion/renderizador_vectorial.py
from implementacion.renderizador import Renderizador

class RenderizadorVectorial(Renderizador):
    """
    CONCEPTO: "Pueden desarrollarse de manera independiente".
    
    Lógica concreta de dibujo mediante vectores matemáticos.
    """
    def dibujar_circulo(self, radio: float) -> str:
        return f"[VECTORIAL] Dibujando círculo de radio {radio} usando trazadis SVG."
    
    def dibujar_cuadrado(self, lado) -> str:
        return f"[VECTORIAL] Dibujando cuadrado de lado {lado} usando nodos vectoriales"
    