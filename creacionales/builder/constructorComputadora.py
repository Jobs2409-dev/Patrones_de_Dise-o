# patrones_de_diseño\creacionales\builder\constructorComputadora.py
from abc import ABC, abstractmethod
from producto import Computadora

class ConstructorComputadora(ABC):
    """
    CONCEPTO: "Creación etapa por etapa de un objeto complejo.
    
    Dclara las operaciones atómicas (pasos de emsamblaje) disponible.
    Cualquier constructor que implemente esta interfaz compartirá el
    mismo conjunto de etapas, garantizando el polimorismo.
    """
    @abstractmethod
    def reset(self) -> None:
        # Inicializa una instancia limpia del producto
        pass
    
    # -- ETAPAS DEL PROCESO CREATIVO
    @abstractmethod
    def colocar_cpu(self, modelo:str) -> None:
        pass
    
    @abstractmethod
    def colocar_ram(self, cantidad: str) -> None:
        pass
    
    @abstractmethod
    def colocar_gpu(self, modelo: str) -> None:
        pass
    
    @abstractmethod
    def colocar_almacenamiento(self, capacidad: str) -> None:
        pass
    
    # -- ENTREGA DEL PRODUCTO FINAL
    def obtener_producto(self) -> Computadora:
        """
        CONCEPTO: "La creación final depende de las etapas ejecutadas".
        
        Devuelve el objeto construido y prepara el builder para un nuevo 
        ciclo. 
        """
        pass
        