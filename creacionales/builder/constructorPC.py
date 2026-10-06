# patrones_de_diseño/creacionales/builder/constructorPC.py
from constructorComputadora import ConstructorComputadora
from producto import Computadora

class ConstructorPC(ConstructorComputadora):
    """
    CONCEPTO: "Mismo código de construcción".
    
    Esta clase contiene la lógica real de ensamblado. Al mantener su
    propia instancia interna (`self._computadora`), aísla por completo al
    cliente de los detalles de inicialización del producto.
    """
    def __init__(self):
        self._computadora = None
        self.reset()
        
    def reset(self) -> None: 
        # Se aegura de comenzar siempre con un objeto limpio
        self._computadora = Computadora()
        
    def colocar_cpu(self, modelo: str) -> None:
        # Etapa simple 1
        self._computadora.cpu = modelo
        
    def colocar_ram(self, cantidad:str) -> None:
        # Etapa simple 2
        self._computadora.ram = cantidad
        
    def colocar_gpu (self, modelo: str) -> None:
        # Etapa simple 3 (opcional)
        self._computadora.gpu = modelo
        
    def colocar_almacenamiento(self, capacidad: str) -> None:
        # Etapa simple 4 (opcional)
        self._computadora.almacenamiento = capacidad
        
    def obtener_producto(self) -> Computadora:
        """
        CONCEPTO: "Independiente de otros objetos".
        
        Entrega la instancia lista, desacoplada de cualquier construcción
        previa o futura.
        """
        producto_terminado = self._computadora
        self.reset() # Queda preparado para construir otra representación.
        return producto_terminado
        
