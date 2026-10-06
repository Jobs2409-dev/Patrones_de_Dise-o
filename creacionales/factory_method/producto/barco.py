# patrones_de_diseño/creacionales/factory_method/producto/barco.py
from interfaces.transporte import Transporte

class Barco(Transporte):
    def entregar(self) -> str:
        return "Entregar por BARCO"