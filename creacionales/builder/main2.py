# patrones_de_diseño\creacionales\builder\main2.py
from constructorPC import ConstructorPC

if __name__ == "__main__":
    # Una única instancia del builder reutilizable
    builder = ConstructorPC()
    
    # REPRESENTACION 1: pc de oficina --
    # CONCEPTO: "La creación final depende de las etapas del
    # proceso creativo"
    # -> Omitimos gpu y usmaos especificaciones base.
    print("== PROCESO 1: PC de oficina ==")
    builder.colocar_cpu("Intel core i3-12100")
    builder.colocar_ram("8 GB DDR4")
    builder.colocar_almacenamiento("256 GB SSD")
    
    # Se guarda la primera representación
    pc_oficina = builder.obtener_producto()
    print(pc_oficina.especificaciones())
    
    # REPRESENTACION 2: pc gamer --
    # CONCEPTO: "Diferentes tipos y representaciones utilizando el mismo
    # código".
    # -> Con el mismo builder, invocamos etapas adicionales y valores de alto
    # rendimiento.
    print("\n== PROCESO 2: PC Gamer ==")
    builder.colocar_cpu("Intel core i7-12700K")
    builder.colocar_ram("32 GB DDR4")
    builder.colocar_almacenamiento("1 TB SSD")
    builder.colocar_gpu("NVIDIA RTX 3080")
    
    # Se genera una representación completamente distinta sin colisionar
    # con lA ANTERIOR
    pc_gamer = builder.obtener_producto()
    print(pc_gamer.especificaciones())
    
    
    print("\nPRUEBA")
    print(pc_oficina.especificaciones())