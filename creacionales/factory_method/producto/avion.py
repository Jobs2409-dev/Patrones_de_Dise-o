# patrones_de_diseño/creacionales/factory_method/producto/avion.py
from interfaces.transporte import Transporte

class Avion(Transporte):
    def entregar(self) -> str:
        return "Entregar por AVIÓN."