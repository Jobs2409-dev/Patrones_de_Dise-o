# patrones_de_diseño/de_comportamiento/command/base_command.py

from abc import ABC, abstractmethod


class Comando(ABC):
    """
    CONCEPTO: Convierte una solicitud en un objeto independiente que contiene
    toda la información sobre la solicitud.
    """

    @abstractmethod
    def ejecutar(self) -> None:
        """
        Ejecuta la solicitud encapsulada.
        """
        pass

    @abstractmethod
    def deshacer(self) -> None:
        """
        CONCEPTO: Respaldar operaciones que no se pueden deshacer (Undo).
        """
        pass