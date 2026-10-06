# patrones_de_diseño/estructurales/flyweigth/main.py
from contexto.bosque import Bosque
from flyweigths.arbol_factory import ArbolFactory

if __name__ == "__main__":
    print("\n=== PATRÓN ESTRUCTURAL: FLYWEIGHT ===\n")
    
    bosque = Bosque()
    
    # Plantamos varios en dierentes coordenadas
    print("-- PLANTANDO PINOS --")
    bosque.plantar_arbol(x=10, y=20, especie="Pino Silvestre", color="Verde Oscuro", textura="textura_pino_4k.png")
    bosque.plantar_arbol(x=15, y=25, especie="Pino Silvestre", color="Verde Oscuro", textura="textura_pino_4k.png")
    bosque.plantar_arbol(x=30, y=80, especie="Pino Silvestre", color="Verde Oscuro", textura="textura_pino_4k.png")

    # Plantamos robles
    print("\n--- PLANTANDO ROBLES ---")
    bosque.plantar_arbol(x=50, y=100, especie="Roble Blanco", color="Verde Claro", textura="textura_roble_4k.png")
    bosque.plantar_arbol(x=60, y=110, especie="Roble Blanco", color="Verde Claro", textura="textura_roble_4k.png")
    
    # Renderizado
    print("\n--- RENDERIZANDO EL BOSQUE ---")
    bosque.renderizar()
    
    # =========================================================================
    # VERIFICACIÓN DE OPTIMIZACIÓN DE MEMORIA
    # =========================================================================
    print("\n" + "=" * 45)
    print(f"Total de árboles plantados en el mapa: {bosque.cantidad_arboles()}")
    print(f"Total de objetos 'TipoArbol' reales en memoria RAM: {ArbolFactory.total_tipo_creados()}")
    print("=" * 45)