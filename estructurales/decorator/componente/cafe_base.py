# patrones_de_diseño/estructurales/decorator/componente/cafe_base.py
from interfaces.bebida import Bebida

class CafeSimple(Bebida):
    """
    CONCEPTO: "La clase inicial permanece inalterada".
    
    Esta clase no sabe nada sobre leche, canela ni ningún agregado.
    Solo se encarga de su propia funcionalidad base.
    """
    def obtener_costo(self) -> float:
        return 100.0
    
    def obtener_descripcion(self) -> str:
        return "Café Solo"
    