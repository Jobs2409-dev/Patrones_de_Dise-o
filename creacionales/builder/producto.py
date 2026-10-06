# patrones_de_diseño\creacionales\builder\producto.py
class Computadora: 
    """
    CONCEPTO: "Objeto complejo combinando objetos simples".
    
    Esta clase representa el producto final. Es independiente del proceso
    de fabricación: no sabe como se eligen ni como se válidan sus partes,
    solo almacena los componentes que las etapas asignan. 
    """
    
    def __init__(self):
        # Arranca con valores por defecto (evita constructores con +8 parametros)
        self.cpu = None
        self.ram = None
        self.almacenamiento = None
        self.gpu = None
        self.refrigeracion_liquida = False
        self.bluetooth = False
        
    
    def especificaciones(self) -> str:
        """"
        Devuelve una vista legible de la represetnación final obtenida
        """
        detalles = [
            f"CPU: {self.cpu}",
            f"RAM: {self.ram}",
            f"Almacenamiento: {self.almacenamiento if self.almacenamiento else 'No asignado'}",
            f"GPU: {self.gpu if self.gpu else 'Integrada'}",
            f"Refrigeración Líquida: {'Sí' if self.refrigeracion_liquida else 'No'}",
            f"Bluetooth: {'Sí' if self.bluetooth else 'No'}"
        ]
        
        return "\n -" + "\n -".join(detalles)