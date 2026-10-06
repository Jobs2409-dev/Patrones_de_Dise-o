# patrones_de_diseño/creacionales/factory_method/producto/camion.py
from interfaces.transporte import Transporte

class Camion(Transporte):
    def entregar(self) -> str:
        return "Entregar por CAMIÓN."