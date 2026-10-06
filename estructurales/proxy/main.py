# patrones_de_diseño/estructurales/proxy/main.py
from interfaces.elemento_multimedia import ElementoMultimedia
from proxies.proxy_imagen import ProxyImagen 

def vison_galeria(elemento: ElementoMultimedia) -> None:
    """
    El cliente interactúa exclusivamente a través de la interfaz común.
    No sabe si está hablando con el objeto real o con su proxy.
    """
    elemento.mostrar()
    
if __name__ == "__main__":
    print("=== PATRÓN ESTRUCTURAL: PROXY ===\n")
    
    # 1. Creamos el proxy.
    # Notar que aquí NO se cargan los 2 GB en RAM, la creación es intantánea.
    print("Paso 1: Obteniendo refencia a la imagen...")
    imagen_proxy = ProxyImagen("fotografia_especial_4k.raw")
    print("Referencia creada sin costo de memoria.")
    
    # 2. Primera solicitud de visualización: el proxy dispara la carga real
    print("\nPaso 2: Usuario abre la imagen por primera vez:")
    vison_galeria(imagen_proxy)
    
    # 3. Segunda solicitud: el proxy ya tiene el objeto en memoria y evita la recarga
    print("\nPaso 3: Usuario abre la misma iamgen nuevamente:")
    vison_galeria(imagen_proxy)