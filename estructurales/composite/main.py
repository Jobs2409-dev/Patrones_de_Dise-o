# patrones_de_diseño/estructurales/composite/main.py
from interfaces.componente_pedido import ComponentePedido
from hoja.producto import Producto
from compuesto.caja import Caja

def calcular_total_pedido(item: ComponentePedido) -> None:
    """
    CONCEPTO: "Trabajar con estas estructuras como si fueran objetos
    individuales".
    
    Al cliente no le importa si recibe un Producto individual o una Caja
    con 10 subcajas anidadas. solo le pide 'obtener_precio()'.
    """
    print(f"--> TOTAL a facturar por '{type(item).__name__}: ${item.obtener_precio()}\n")
    
    
if __name__ == "__main__":
    print("== PATRÓN ESTRUCTURAL: COMPOSITE ==\n")
    
    # 1. creamos objetos simples (Hojas)
    mouse = Producto(nombre="Mouse Gamer", precio=15.0)
    teclado = Producto(nombre="Teclado Mecánico", precio=30.0)
    auricular = Producto(nombre="Auriculares", precio=50.00)
    pendrive = Producto(nombre="Pendrive 64GB", precio=10.0)
    cable = Producto(nombre="Cable USB-C", precio=5.0)
    
    
    # 2. Armamos la estructura de árbol
    # Sub-Caja de accesorios
    caja_cables = Caja(nombre="Caja de accesorios Chicos")
    caja_cables.agregar(pendrive)
    caja_cables.agregar(cable)
    
    # Caja principal que contiene productos directos y subcajas
    caja_naivdena = Caja(nombre="Caja Navideña Gamer")
    caja_naivdena.agregar(auricular)
    caja_naivdena.agregar(teclado)
    caja_naivdena.agregar(caja_cables)
    
    # 3. Visualizamos la estructura
    print("ESTRUCTURA DEL ÁRBOL:")
    caja_naivdena.mostrar_detalle()
    print("_"*40)
    
    # 4. Tratamiento uniforme: calcular precio de un objeto simple vs un compuesto 
    print("1. Cobrando un producto simple:")
    calcular_total_pedido(mouse)
    
    print("2. Cobrando un árbol compuesto completo:")
    calcular_total_pedido(caja_naivdena)   