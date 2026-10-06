# patrones_de_diseño/estructurales/decorator/main.py
from componente.cafe_base import CafeSimple
from decoradores.decorador_leche import ConLeche
from decoradores.decoradot_canela import ConCanela

if __name__ == "__main__":
    print("=== PATRÓN ESTRUCTURAL: DECORATOR ===\n")
    
    # 1. objeto base inalterado
    mi_cafe = CafeSimple()
    print(f"Pedido 1: {mi_cafe.obtener_descripcion()} -> ${mi_cafe.obtener_costo()}")
    
    
    # 2. Le agregamos leche envolviendo el objeto base
    # La clase CafeSimple no se modificó en nada
    cafe_con_leche = ConLeche(mi_cafe)
    print(f"Pedido 2: {cafe_con_leche.obtener_descripcion()} -> ${cafe_con_leche.obtener_costo()}")
    
    # 3. Le agregamos canela arriba del café que ya tenía Leche (apilamiento)
    cafe_completo = ConCanela(cafe_con_leche)
    print(f"Pedido 3: {cafe_completo.obtener_descripcion()} -> ${cafe_completo.obtener_costo()}")
    
    