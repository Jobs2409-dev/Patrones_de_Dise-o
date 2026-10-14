# patrones_de_diseño/de_comportamiento/command/invoker.py

from typing import List
from base_command import Comando


class PanelControl:
    """
    INVOCADOR:
    CONCEPTO: Permite parametrizar métodos con diferentes solicitudes,
    retrasar o poner en cola la ejecución de una solicitud y respaldar
    operaciones que no se pueden deshacer.
    """

    def __init__(self):
        self._cola_solicitudes: List[Comando] = []
        self._historial_ejecutados: List[Comando] = []

    def agregar_a_cola(self, comando: Comando) -> None:
        """
        CONCEPTO: Retrasar o poner en cola la ejecución de una solicitud.
        """
        self._cola_solicitudes.append(comando)
        print("[PANEL] Solicitud agregada a la cola de ejecución.")

    def ejecutar_cola(self) -> None:
        """
        Procesa de forma secuencial todas las solicitudes almacenadas.
        """
        print("\n--- INICIANDO EJECUCIÓN DE COLA ENCOLADA ---")
        while self._cola_solicitudes:
            cmd = self._cola_solicitudes.pop(0)
            cmd.ejecutar()
            self._historial_ejecutados.append(cmd)

    def deshacer_ultima_operacion(self) -> None:
        """
        CONCEPTO: Respaldar operaciones que no se pueden deshacer (Undo).
        """
        if self._historial_ejecutados:
            ultimo_comando = self._historial_ejecutados.pop()
            print("\n--- DESHACIENDO ÚLTIMA OPERACIÓN ---")
            ultimo_comando.deshacer()
        else:
            print("[PANEL] No hay operaciones registradas para deshacer.")