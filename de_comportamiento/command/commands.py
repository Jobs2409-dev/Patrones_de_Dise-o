# patrones_de_diseño/de_comportamiento/command/commands.py

from base_command import Comando
from receiver import SistemaSuministros


class ComandoRiego(Comando):
    """
    CONCEPTO: Objeto independiente que contiene la solicitud de riego.
    """

    def __init__(self, receptor: SistemaSuministros, zona: str):
        self._receptor = receptor
        self._zona = zona

    def ejecutar(self) -> None:
        self._receptor.activar_riego(self._zona)

    def deshacer(self) -> None:
        self._receptor.desactivar_riego(self._zona)


class ComandoIluminacion(Comando):
    """
    CONCEPTO: Objeto independiente que contiene la solicitud de iluminación.
    """

    def __init__(self, receptor: SistemaSuministros, modulo_id: int):
        self._receptor = receptor
        self._modulo_id = modulo_id

    def ejecutar(self) -> None:
        self._receptor.encender_iluminacion(self._modulo_id)

    def deshacer(self) -> None:
        self._receptor.apagar_iluminacion(self._modulo_id)