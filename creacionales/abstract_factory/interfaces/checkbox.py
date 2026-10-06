# patrones_de_diseño\creacionales\abstract_factory\interfaces_productos\checkbox.py
from abc import ABC, abstractmethod

"""
CONCEPTO: "Objeto relacionados" (Componente 2).

Segundo miembro de la familia de componentes graficos.
Garantiza que cualquier casilla de verificación cumpla con el método
render().
"""
class Checkbox(ABC):
    # RESPONSABILIDAD ÚNICA: Definir el contrato formal exclusivo para los
    # los objetos de tipo Checkbox.
    def render(self) -> str:
        # Dibuja el checkbox en pantalla.
        pass