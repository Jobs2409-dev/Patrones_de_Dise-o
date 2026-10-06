# patrones_de_diseño/creacionales/factory_method/main3.py
from creadores.logistica_base import Logistica
from creadores.logistica_aire import LogisticaAire
from creadores.logistica_mar import LogisticaMar
from creadores.logistica_tierra import LogisticaTierra

def ejecutar_operacion(logistica: Logistica) -> None:
    """
    El cliente interactua con la superclase Logistica.
    No conoce Camion, Barco ni Avion; solo ejecuta el flujo de
    trabajo general.
    """
    print(logistica.planificar_entrega())
    
    
    
if __name__ == "__main__":
    print("-- LOGÍSTICA POR TIERRA --")
    logistica_tierra = LogisticaTierra()
    ejecutar_operacion(logistica_tierra)
    
    print("\n-- LOGÍSTICA POR AIRE --")
    logistica_aire = LogisticaAire()
    ejecutar_operacion(logistica_aire)
    
    print("\n-- LOGÍSTICA POR AGUA --")
    logistica_agua = LogisticaMar()
    ejecutar_operacion(logistica_agua)
    