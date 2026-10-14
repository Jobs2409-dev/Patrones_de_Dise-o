# patrones_de_diseño/de_comportamiento/chain_of_responsibility/base_handler.py
from abc import ABC, abstractmethod
from typing import Optional
from models import PeticionAlerta


class ManejadorBase(ABC):
    """
    CONCEPTO: Evita acoplar el emisor de una petición a su receptor.
    Define la interfaz para procesar las peticiones y mantiene la referencia
    al siguiente objeto receptor en la cadena.
    """

    def __init__(self, siguiente: Optional["ManejadorBase"] = None):
        # Referencia al siguiente objeto receptor posible
        self._siguiente: Optional[ManejadorBase] = siguiente

    def establecer_siguiente(
        self, siguiente: "ManejadorBase"
    ) -> "ManejadorBase":
        """
        Permite conectar los objetos receptores en una secuencia (cadena).
        """
        self._siguiente = siguiente
        return siguiente

    @abstractmethod
    def responder_peticion(self, peticion: PeticionAlerta) -> None:
        """
        CONCEPTO: Método donde cada receptor evalúa la posibilidad de
        responder a la petición.
        """
        pass

    def _delegar_al_siguiente(self, peticion: PeticionAlerta) -> None:
        """
        Pasa la petición al siguiente receptor si existe en la cadena.
        """
        if self._siguiente:
            self._siguiente.responder_peticion(peticion)
        else:
            print(
                f"[FIN DE CADENA] Ningún receptor pudo responder a la petición: {peticion}"
            )