# patrones_de_diseño/creacionales/prototype/prototipo/personaje.py
import copy
from interfaces.prototipo import Prototipo

class Personaje(Prototipo):
    # Representa una entidad de personaje independiente
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        
    def clonar(self) -> "Personaje":
        return copy.deepcopy(self)

    def mostrar_personaje(self) -> str:
        return f"Personaje: {self.nombre} | Edad: {self.edad}"