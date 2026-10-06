# patrones_de_diseño/estructurales/proxy/servicios_reales/imagen_alta_resolucion.py
import time
from interfaces.elemento_multimedia import ElementoMultimedia

class ImagenAltaResolucion(ElementoMultimedia):
    """
    CONCEPTO: "Funciones de otras clases u objetos".
    
    Sujeto Real: Hace el trabajo pesado real. En su inicialización
    simula una carga costosa desde el disco o red (2GB de datos).
    """
    def __init__(self, archivo: str):
        self.archivo = archivo
        self._cargar_desde_disco()
    
    def _cargar_desde_disco(self) -> None:
        print(f"--> [Disco] Cargando archivo pesado '{self.archivo}' (2 GB en RAM)...")
        time.sleep(1.0) # Simula demora de I/O
        print(f"--> [Disco] '{self.archivo}' cargada completamente en memoria.")
        
    
    def mostrar(self) -> None:
        print(f"[Pantalla] Renderizando imagen HD: '{self.archivo}'")