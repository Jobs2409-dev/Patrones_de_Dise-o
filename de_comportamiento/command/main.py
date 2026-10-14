# patrones_de_diseño/de_comportamiento/command/main.py

from receiver import SistemaSuministros
from commands import ComandoRiego, ComandoIluminacion
from invoker import PanelControl


def ejecutar_demo():
    # 1. Crear el receptor de las acciones
    sistema_planta = SistemaSuministros()

    # 2. CONCEPTO: Convertir solicitudes en objetos independientes
    cmd_riego = ComandoRiego(sistema_planta, zona="Módulo Sector Norte")
    cmd_luz = ComandoIluminacion(sistema_planta, modulo_id=2)

    # 3. Crear el invocador (Panel de Control)
    panel = PanelControl()

    # 4. CONCEPTO: Parametrizar métodos retrasando o poniendo en cola la ejecución
    print("--- PASO 1: Encolar Solicitudes ---")
    panel.agregar_a_cola(cmd_riego)
    panel.agregar_a_cola(cmd_luz)

    # 5. Ejecutar la cola diferida
    panel.ejecutar_cola()

    # 6. CONCEPTO: Respaldar operaciones que no se pueden deshacer
    panel.deshacer_ultima_operacion()


if __name__ == "__main__":
    ejecutar_demo()