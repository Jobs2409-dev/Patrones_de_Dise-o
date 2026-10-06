# patrones_de_diseño/estructurales/facade/subsitemas/amplificador.py

class AmplificadorAudio:
    """
    CONCEPTO: "Conjunto complejo de clases".
    
    Maneja detalles técnicos del hardware de sonido.
    """
    def encender(self) -> None:
        print("[Audio] Amplificador encendido.")
        
        
    def configurar_volumen(self, nivel: int) -> None:
        print(f"[Audio] Volumen calibrado al nivel {nivel}.")
        
    def apagar(self) -> None:
        print("[Audio] Amplificador apagado.")