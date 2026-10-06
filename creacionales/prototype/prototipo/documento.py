# patrones_de_diseño/creacionales/prototype/prototipo/documento.py
import copy
from interfaces.prototipo import Prototipo

class Documento(Prototipo):
    """
    CONCEPTO: "Restringir operaciones manteniendo la modificación al 
    mínimo utilizando copias de objetos."
    
    Representa un documento editable. Contiene atributos complejos
    y mutables.
    """
    def __init__(self, titulo: str, autor: str, etiquetas: list[str]):
        self.titulo: str = titulo
        self.autor: str = autor
        # Estructura mutable: Si hicieramos copiuas superficiales (shallow),
        # el clon y el original compartirían la misma lista en memoria.
        self.etiquetas: list[str] = etiquetas
        
    def clonar(self) -> "Documento":
        """
        CONCEPTO: "Auto-duplicación profunda (deep copy)".
        
        Delega en la propia instancia la responsabilidad de duplicarse
        completa e independientemente en memoria.
        """
        return copy.deepcopy(self)
    
    def mostrar_info(self) -> str:
        return f"Titulo: '{self.titulo}' | Autor: '{self.autor}' | Etiquetas: '{self.etiquetas}'"
            