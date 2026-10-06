# patrones_de_diseño/estructurales/composite/compuesto/caja.py
from interfaces.componente_pedido import ComponentePedido

class Caja(ComponentePedido):
    """
    CONCEPTO: 
    1) "Se usa para agurpar objetos como un solo objeto".
    2) "Permite componer objetos en estructuras de árbol".
    
    Esta clase (Composite) contiene una lista de  'ComponentePedido'.
    Al implementar la misma interfaz, puede contener Productos y también
    otras Cajas.
    """
    def __init__(self, nombre: str):
        self.nombre=nombre
        self._hijo: list[ComponentePedido] = []
        
    def agregar(self, componente: ComponentePedido) -> None:
        # Agregar un elemento (hoja o sub-árbol) a la estructura.
        self._hijo.append(componente)
            
    def eliminar(self, componente: ComponentePedido) -> None:
        self._hijo.remove(componente)
            
    def obtener_precio(self) -> float:
        """
        CONCEPTO: Trata la colección como un solo objeto.
        
        Calcula el total sumado recursivamente el precio de todos sus
        elementos.
        """
        total = 0.0
        for hijo in self._hijo:
            total += hijo.obtener_precio()
                
        return total
        
    def mostrar_detalle(self, nivel: int = 0) -> None:
        sangria = " " * nivel
        print(f"{sangria}+ [Caja: {self.nombre}] (Total parcial: ${self.obtener_precio()})")
        for hijo in self._hijo:
            hijo.mostrar_detalle(nivel + 1)
            
        
    