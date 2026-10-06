# patrones_de_diseño/estructurales/facade/subsitemas/proyectar.py

class ProyectarVideo:
    """
    CONCEPTO: "Conjunto complejo de clases".
    
    Control del poryector y entrada de video.
    """
    def encender(self) -> None:
        print("[Video] Proyector iniciado en resolución 4K.")

    def reproducir_contenido(self, titulo: str) -> None:
        print(f"[Video] Transmitiendo: '{titulo}'.")
        
    def apagar(self) -> None:
        print("[Video] Proyector apagado.")    