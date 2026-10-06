# patrones_de_diseño/estructurales/decorator/decoradores/decorador_leche.py
from decoradores.base_decorador import DecoradorBase

class ConLeche(DecoradorBase):
    """
    CONCEPTO: "Agrega una nueva funcionalidad / capacidad adicional".
    
    Suma su comportamiento específico sobre la llamada delegada.
    """
    def obtener_costo(self) -> float:
        # Costo del objeto que tiene adentro + su propio extra
        return self._bebida.obtener_costo() + 30.0
    
    def obtener_descripcion(self) -> str:
        return f"{self._bebida.obtener_descripcion()} + Leche"
    