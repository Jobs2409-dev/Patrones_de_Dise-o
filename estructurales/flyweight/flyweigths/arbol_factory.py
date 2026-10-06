# patrones_de_diseño/estructurales/flyweigth/flyweigths/arbol_factory.py
from flyweigths.tipo_arbol import TipoArbol

class ArbolFactory:
    """
    CONCEPTO: "El patrón busca objetos similares que ya existen para
    reutilizarlo en lugar de crear otros nuevos".
    
    Administra la caché de flyweights para garantizar que nunca se 
    dupliquen objetos con el mismo estado intrínseco en memoria.
    """
    _tipo_arbol: dict[str, TipoArbol] = {}
    
    @classmethod
    def obtener_tipo_arbol(cls, especie: str, color: str, textura_datos : str) -> TipoArbol:
        clave = f"{especie}_{color}"
        
        # So ya existe en el diccionario/caché, lo reutilizo directamente
        if clave not in cls._tipo_arbol:
            print(f"--> [Factory] Creando en memoria un nuevo TipoArbol: '{especie}' ({color})")
            cls._tipo_arbol[clave] = TipoArbol(especie, color, textura_datos)
        else:
            print(f"--> [Factory] Reutilizando instancia existente en memoria para: '{especie}'")
            
        return cls._tipo_arbol[clave]
        
        
    @classmethod
    def total_tipo_creados(cls) -> int:
        return len(cls._tipo_arbol)