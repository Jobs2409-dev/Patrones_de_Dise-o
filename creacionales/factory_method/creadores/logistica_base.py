# patrones_de_diseño/creacionales/factory_method/creadores/logistica_base.py
from abc import ABC, abstractmethod
from interfaces.transporte import Transporte

class Logistica(ABC):
    """
    CONCEPTO: "Proporciona una interaz para crear objetos en una 
    superclase"
    
    La superclase NO sabe qué concreto se creará en tiempo de ejecución.
    Solo define la lógica de negocio principal y confía en el Factory
    Methods.
    """
    @abstractmethod
    def crear_transporte(self) -> Transporte:
        """
        ESTE ES EL FACTORY METHOD.
        
        Las subclases están obligadas a sobreeescrbir para decidir la 
        instancia concreta a devolver.
        """
        
        pass
    
    def planificar_entrega(self) -> str:
        """
        CONCEPTO: "Instanciación de objetos implicíta a través de 
        interfaces comunes".
        
        Aquí se evidencia el patrón: La superclase llama implicítamente a 
        `self.crear_transporte()`. No hace un new `Camion()` directo;
        opera sobre la interaz común `Transporte`
        """
        transporte = self.crear_transporte()
        return f"Logística: Se inició el envio -> {transporte.entregar()}"
        
        