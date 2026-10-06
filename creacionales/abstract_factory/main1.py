# patrones_de_diseño/creacionales/abstract_factory/main1.py
from interfaces.fabrica_gui import FabricaGUI
from fabrica.fabrica_azul import FabricaTemaAzul
from fabrica.fabrica_claro import FabricaTemaClaro
from fabrica.fabrica_oscuro import FabricaTemaOscuro

def renderizar_interfaz(fabrica: FabricaGUI) -> None:
    """
    CONCEPTO: "Sin especificar el nombre de la clase"
.
    Código del cliente: Trabaja solo con la abstracción (FabricaGUI).
    El cliente pide los componentes a la fabrica recibida y los utiliza 
    usando el método garantizado por el contrato (render), sin importar
    si detrás hay un tema claro, oscuro o azul.
    """
    boton = fabrica.crear_boton()
    checkbox = fabrica.crear_checkbox()
    
    print(boton.render())
    print(checkbox.render())
    

if __name__ == "__main__":
    print("--PROBANDO INTERFAZ EN MODO CLARO--")
    fabrica_claro = FabricaTemaClaro()
    renderizar_interfaz(fabrica_claro)
    
    print("\n--PROBANDO INTERFAZ EN MODO OSCURO--")
    fabrica_oscuro = FabricaTemaOscuro()
    renderizar_interfaz(fabrica_oscuro)
        
    print("\n--PROBANDO INTERFAZ EN MODO AZUL--")
    fabrica_azul = FabricaTemaAzul()
    renderizar_interfaz(fabrica_azul)