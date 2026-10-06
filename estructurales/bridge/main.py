# patrones_de_diseño/estructurales/bridge/main.py
from implementacion.renderizador_vectorial import RenderizadorVectorial
from implementacion.renderizador_raster import RenderizadorRaster
from abstraccion.circulo import Circulo
from abstraccion.cuadrado import Cuadrado

if __name__ == "__main__":
    print("== PATRÓN ESTRUCTURAL: BRIDGE ==\n")
    # 1. Definimos las implementaciones disponibles
    motor_vectorial =  RenderizadorVectorial()
    motor_raster = RenderizadorRaster()
    
    
    # 2. Conectamos libremente abstracción con implemnetaciones vía el puente
    # Mismo círculo, dos tecnologías distintas sin crear subclases adicionales
    circulo_vector = Circulo(radio=5.0, renderizador=motor_vectorial)
    circulo_pixel = Circulo(radio=5.0, renderizador=motor_raster)
    
    print(circulo_vector.dibujar())
    print(circulo_pixel.dibujar())
    
    print("\n== CUADRADO CON MOTOR VECTORIAL ==")
    Cuadrado_vector = Cuadrado(lado=10.0, renderizador=motor_vectorial)
    print(Cuadrado_vector.dibujar())
     