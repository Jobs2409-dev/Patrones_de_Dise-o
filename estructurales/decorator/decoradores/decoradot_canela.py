# patrones_de_diseño/estructurales/decorator/decoradores/decoradot_canela.py
from decoradores.base_decorador import DecoradorBase

class ConCanela(DecoradorBase):
    """
    CONCEPTO: "Agrega una nueva funcionalidad / capacidad adiconal".
    """
    def obtener_costo(self) -> float:
        # Costo del objeto que tiene adentro + su propio extra
        return self._bebida.obtener_costo() + 15.0
    
    def obtener_descripcion(self) -> str:
        return f"{self._bebida.obtener_descripcion()} + Canela"