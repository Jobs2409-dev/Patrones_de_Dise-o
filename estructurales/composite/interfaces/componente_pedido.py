# patrones_de_diseño/estructurales/composite/interfaces/componente_pedido.py
from abc import ABC, abstractmethod

class ComponentePedido(ABC):
    """
    CONCEPTO: "Trabajar con estas estructuras como si fueran objetos
    individuales"
    
    Estas interfaces establecen el contrato tanto para elementos simples
    (hojas). El cliente interactúa solo con esto.
    """
    @abstractmethod
    def obtener_precio(self) -> float:
        # Devuelve el costo del componente, sea individual o una colección.
        pass
    
    @abstractmethod
    def mostrar_detalle(self, nivel: int) -> None:
        # Muestra la jerarquía en la estructura ásrbol.
        pass
    