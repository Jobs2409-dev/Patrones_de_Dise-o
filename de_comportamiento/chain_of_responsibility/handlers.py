# patrones_de_diseno/de_comportamiento/chain_of_responsibility/handlers.py
from base_handler import ManejadorBase
from models import PeticionAlerta


class OperadorMonitoreo(ManejadorBase):
    """
    CONCEPTO: Primer objeto receptor con posibilidad de responder a la petición.
    Atiende peticiones de severidad 1.
    """

    def responder_peticion(self, peticion: PeticionAlerta) -> None:
        if peticion.nivel_severidad == 1:
            print(
                f"[Operador Monitoreo] PETICIÓN RESUELTA: '{peticion.descripcion}' atendida en ronda básica."
            )
        else:
            print(
                f"[Operador Monitoreo] Severidad {peticion.nivel_severidad} excede mi rango. Escalando petición..."
            )
            self._delegar_al_siguiente(peticion)


class SupervisorModulo(ManejadorBase):
    """
    CONCEPTO: Segundo objeto receptor con posibilidad de responder a la petición.
    Atiende peticiones de severidad 2.
    """

    def responder_peticion(self, peticion: PeticionAlerta) -> None:
        if peticion.nivel_severidad == 2:
            print(
                f"[Supervisor Módulo] PETICIÓN RESUELTA: '{peticion.descripcion}' gestionada en módulo."
            )
        else:
            print(
                f"[Supervisor Módulo] Severidad {peticion.nivel_severidad} excede mi rango. Escalando petición..."
            )
            self._delegar_al_siguiente(peticion)


class DirectorEmergencias(ManejadorBase):
    """
    CONCEPTO: Tercer objeto receptor con posibilidad de responder a la petición.
    Atiende peticiones de severidad 3.
    """

    def responder_peticion(self, peticion: PeticionAlerta) -> None:
        if peticion.nivel_severidad == 3:
            print(
                f"[Director Emergencias] PETICIÓN RESUELTA: Protocolo crítico activado para '{peticion.descripcion}'."
            )
        else:
            print(
                f"[Director Emergencias] Severidad {peticion.nivel_severidad} fuera de protocolo. Escalando petición..."
            )
            self._delegar_al_siguiente(peticion)