# patrones_de_diseño/estructurales/composite/hoja/producto.py
from interfaces.componente_pedido import ComponentePedido

class Producto(ComponentePedido):
    """
    CONCEPTO: "Objetos individuales."
    
    Representa una 'Hoja' (Leaf) en la estructura de árbol.
    No contiene a otros componentes; tiene su propio precio diferente.
    """
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
        
    def obtener_precio(self) -> float: 
        return self.precio
        
    def mostrar_detalle(self, nivel: int=0) -> None:
        sangria = " " * nivel
        print(f"{sangria}- Producto: {self.nombre} (${self.precio})")
    