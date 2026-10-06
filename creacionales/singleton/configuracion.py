# patrones_de_diseño/creacionales/singleton/configuracion.py
from singleton_meta import SingletonMeta

class Configuracion(metaclass=SingletonMeta):
    """
    Gestiona el estado global de configuración de la aplicación.

    Gracias a 'metaclass=SingletonMeta', esta clase queda automáticamente
    restringida a un único objeto en toda la ejecución, sin ensuciar su
    lógica interna con validaciones de memoria.
    """
    def __init__(self):
        self.idioma: str = "ES"
        self.modo_oscuro: bool = False
        
    def actualizar_parametros(self, idioma: str, modo_oscuro: bool) -> None:
        """Modificar el estado del recurso compartido."""
        self.idioma = idioma
        self.modo_oscuro = modo_oscuro
        
    def obtener_estado(self) -> str:
        """Devuleve una vista legible de la coniguración actual."""
        return f"Idioma: {self.idioma} | Modo Oscuro: {'Activado' if self.modo_oscuro else 'Desactivado'}."

