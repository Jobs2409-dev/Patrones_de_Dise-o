# patrones_de_diseño/estructurales/facade/main.py
from subsitemas.amplificador import AmplificadorAudio
from subsitemas.luces import SistemaLuces
from subsitemas.proyectar import ProyectarVideo
from fachada.fachada_cine import FachadaEnCasa

if __name__ == "__main__":
    print("=== PATRÓN ESTRUCTURAL: FACADE ===\n")
    
    # 1. Instancíamos los componentes del subsitema complejo
    sistema_audio = AmplificadorAudio()
    sistema_luces = SistemaLuces()
    sistema_video = ProyectarVideo()
    
    # 2. Inicializamos la fachada que los agrupa
    cine_en_casa = FachadaEnCasa(
        audio=sistema_audio,
        luces=sistema_luces,
        proyector=sistema_video
    )
    
    """
    CONCEPTO: "Interfaz símplificada".
    
    El cliente no tiene que llamar a los 5 métodos técnicos uno por uno;
    solo pide iniciar la película
    """
    cine_en_casa.ver_pelicula("Interestelar")
    
    # Al terminar, otra orden de alto nivel apaga todo
    cine_en_casa.terminar_pelicula()
    