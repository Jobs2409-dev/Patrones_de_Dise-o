# patrones_de_diseño/estructurales/proxy/proxies/proxy_imagen.py
from interfaces.elemento_multimedia import ElementoMultimedia
from servicios_reales.imagen_alta_resolucion import ImagenAltaResolucion

class ProxyImagen(ElementoMultimedia):
    """
    CONCEPTO:
    1)_ "Se utiliza para crear objetos que pueden representar funciones
    de otras clases".
    2)_ "La interfaz se utiliza para acceder a estas funcionalidades".
    
    El proxy:
    - Implementa 'ElementoMultimedia' para ser intercambiado con el 
    objeto real.
    - Mantiene una referencia al objeto real (Inicialmente en None).
    - Controla el accesso: posterga la instanciación pesada hasta el primer
    uso (Lazy Loading).
    """
    def __init__(self, archivo: str):
        self.archivo = archivo
        self._imagen_real: ImagenAltaResolucion | None = None
        
    def mostrar(self) -> None:
        """
        CONCEPTO: Representa la función delegada en el objeto real,
        pero agregando control previo sobre su ciclo de vida.
        """
        # Carga perezosa (Lazy Loading): Si no fue creada, se crea ahora
        if self._imagen_real is None:
            print("[Proxy] Primera solicitud detectada: instanciando objeto real bajo demanda...")
            self._imagen_real = ImagenAltaResolucion(self.archivo)
        else:
            print("[Proxy] Reutilizando objeto real ya existente en memoria (sin recargar)...")

        self._imagen_real.mostrar()