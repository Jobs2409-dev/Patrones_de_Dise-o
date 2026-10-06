# patrones_de_diseño/estructurales/adapter/interfaces/procesador_pago.py
from abc import ABC, abstractmethod

class ProcesadorPago(ABC):
    """
    CONCEPTO: "El concepto de herencia se utiliza para componer interfaces".
    
    Esta es la interfaz objetiva (Target). Define el estándar que nuestro
    sistema ya comprende para ejecutar pagos.
    """
    
    @abstractmethod
    def pagar(self, monto: float) -> str:
        # Método estándar de pago que espera nuestro código cliente.
        pass
        