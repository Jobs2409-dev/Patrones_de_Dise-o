# patrones_de_diseño/creacionales/prototype/main4.py
from prototipo.documento import Documento
from prototipo.personaje import Personaje

if __name__ == "__main__":
    # CASO 1: Documento y verificación de mutabilidad independeiente
    print("=== 1. OBJETO ORIGINAL (PLANTILLA BASE) ===")
    plantilla = Documento(
        titulo="Reporte Mensulal",
        autor="Jonathan",
        etiquetas=["finanzas", "2026", "borrador"]
    )
    print(plantilla.mostrar_info())
    
    
    print("\n=== 2. CLONACIÓN Y MODIFICACIÓN MÍNIMA ===")
    """
    CONCEPTO: "En lugar de volver a consultar una base de datos o 
    instanciar con todos los parámetros, duplicamos la plantilla 
    existente".
    """
    reporte_abril = plantilla.clonar()
    reporte_abril.titulo = "Reporte Mensual - ABRIL"
    reporte_abril.etiquetas.append("revisado") # modificamos la lista mutable
    print(f"Clon modificado-. {reporte_abril.mostrar_info()}")
    
    
    print("\n=== 3. VERIFICACIÓN DE INDEPENDENCIA EN MEMORIA ===")
    # El original debe conservar intacta su lsita de etiqueta
    print(f"Original Intacta: {plantilla.mostrar_info()}")
    print(f"¿Comparten la misma lista de etiquetas?: {plantilla.etiquetas is reporte_abril.etiquetas}")
    
    # CASO 2: PEROSNAJE
    print("\n=== 4. PROTOTIPO PERSONAJE ===")
    personaje_base = Personaje(nombre="Jobs", edad=26)
    print(f"Original: {personaje_base.mostrar_personaje()}")
    
    
    personaje_clon = personaje_base.clonar()
    personaje_clon.edad = 25
    print(f"Clon modificado: {personaje_clon.mostrar_personaje()}")
    print(f"Original verificado: {personaje_base.mostrar_personaje()}")
    
    
    