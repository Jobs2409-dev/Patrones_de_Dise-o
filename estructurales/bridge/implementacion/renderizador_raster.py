from implementacion.renderizador import Renderizador

class RenderizadorRaster(Renderizador):
    """
    CONCEPTO: "Pueden desarrollarse de manera independiente".
    
    Lógica concreta de dibujado mediante mapa de bits (pixeles).
    """
    def dibujar_cuadrado(self, lado) -> str:
        return f"[RASTER] Dibujando cuadrado de lado {lado} en una matriz de pixeles."
    
    def dibujar_circulo(self, radio) -> str:
        return f"[RASTER] Dibujando circulo de radio {radio} rellenando pixeles."