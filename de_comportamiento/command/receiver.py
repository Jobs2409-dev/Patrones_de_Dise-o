# patrones_de_diseño/de_comportamiento/command/receiver.py
# patrones_de_diseño/de_comportamiento/command/receiver.py


class SistemaSuministros:
    """
    RECEPTOR: Contiene la lógica real para ejecutar las acciones.
    El comando delegado invocará estos métodos.
    """

    def activar_riego(self, zona: str) -> None:
        print(f"[RECEPTOR] Sistema de Riego ACTIVADO en: '{zona}'.")

    def desactivar_riego(self, zona: str) -> None:
        print(f"[RECEPTOR] Sistema de Riego DESACTIVADO en: '{zona}'.")

    def encender_iluminacion(self, modulo_id: int) -> None:
        print(f"[RECEPTOR] Iluminación ENCENDIDA en Módulo {modulo_id}.")

    def apagar_iluminacion(self, modulo_id: int) -> None:
        print(f"[RECEPTOR] Iluminación APAGADA en Módulo {modulo_id}.")