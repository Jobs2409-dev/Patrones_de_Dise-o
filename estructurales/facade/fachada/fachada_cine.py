# patrones_de_diseño/estructurales/facade/fachada/fachada_cine.py
from subsitemas.amplificador import AmplificadorAudio
from subsitemas.luces import SistemaLuces
from subsitemas.proyectar import ProyectarVideo

class FachadaEnCasa:
    """
    CONCEPTO: "Proporciona una interfaz simplificada para una biblioteca,
               un marco o cualquier otro conjunto complejo de clases".
               
    Ofrece operaciones de alto nivel que coordinan múltiples subsistemas,
    evitando que el cliente deba reconocer los detalles de cada uno.
    """
    def __init__(self, audio: AmplificadorAudio, luces: SistemaLuces, proyector: ProyectarVideo):
        # Mantiene las referencias a los distintos subsistemas
        self._audio = audio
        self._luces = luces
        self._proyector = proyector
        
    def ver_pelicula(self, titulo: str) -> None:
        """
        Método simplificado: En una sola instrucción ejecuta la secuencia
        completa requerida por los 3 subsistemas.
        """
        print(f"\n-- PREPARANDO CINE PARA: '{titulo}' --")
        self._proyector.encender()
        self._audio.encender()
        self._luces.aumentar(15)
    
    
    def terminar_pelicula(self) -> None:
        """
        Método simplificador de apagado.
        """
        print("\n-- FINALIZANDO SESIÓN DE CINE --")
        self._proyector.apagar()
        self._audio.apagar()
        self._luces.encender_completas()
        