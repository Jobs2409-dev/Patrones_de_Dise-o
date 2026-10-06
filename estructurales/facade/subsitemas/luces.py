# patrones_de_diseño/estructurales/facade/subsitemas/luces.py

class SistemaLuces:
    """
    CONCEPTO: "Conjunto complejo de clases".
    
    Control domótico de iluminación de la sala.
    """
    def aumentar(self, porcentaje: int) -> None:
        print(f"[Luces] Ambiente atenuado al {porcentaje}%.")
        
    def encender_completas(self) -> None:
        print("[Luces] Luces de la sala encendidas al 100%.")
    