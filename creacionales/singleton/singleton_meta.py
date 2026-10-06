# patrones_de_diseño/creacionales/singleton/singleton_meta.py
class SingletonMeta(type):
    """
    CONCEPTO: "Restringe la creación de instancias de una clase a un
    único objeto".
    
    Controlar el ciclo de vida e instanicas de cualquier clase que la use.
    Mantiene un diccionario interno de instancias únicas creadas.
    """
    _instancias = {}
    
    def __call__(cls, *args, **kwargs):
        """
        Intercepta la llamada de creación (ej. Configuracion()).
        Si la clase aún no fue instanciada, la crea y la almacena.
        Si ya existe, devuelve la referencia existente sin crear una nueva.
        """
        if cls not in cls._instancias:
            instancia = super().__call__(*args, **kwargs)
            cls._instancias[cls] = instancia
            
        return cls._instancias[cls]
        
    