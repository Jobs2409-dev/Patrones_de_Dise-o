# patrones_de_diseño/estructurales/flyweigth/flyweigths/tipo_arbol.py
class TipoArbol:
    """
    CONCEPTO: "Reducir el uso de memoria... reutilizar obetos similares".
    
    ESTADO INTRÍNSECO (Compartido):
    Contiene la información pesada e inmutable (especie, color, datos
    de textura). Muchos árboles en el mapa compartirán exactamente la
    misma instancia de esta clase.
    """
    def __init__(self, especie: str, color: str, textura_dato: str): 
        self.especie = especie
        self.color = color
        self.textura_dato = textura_dato
        
    def dibujar(self, x: int, y: int) -> None:
        """
        CONCEPTO: Recibe el ESTADO EXTRÍNSECO (x, y) por parámetro al 
        momento de operar, en lugar de almacenarlo en su propia memoria.
        """
        print(f"[Render] Árbol '{self.especie}' ({self.color}) dibujado en ({x}, {y}).")
        
        
    