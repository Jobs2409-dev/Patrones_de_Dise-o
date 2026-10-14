# patrones_de_diseno/de_comportamiento/chain_of_responsibility/main.py

from handlers import OperadorMonitoreo, SupervisorModulo, DirectorEmergencias
from models import PeticionAlerta


def ejecutar_demo():
    # 1. Instanciación de los objetos receptores
    monitoreo = OperadorMonitoreo()
    supervisor = SupervisorModulo()
    director = DirectorEmergencias()

    # 2. Configuración de la cadena: Monitoreo -> Supervisor -> Director
    monitoreo.establecer_siguiente(supervisor).establecer_siguiente(director)

    # 3. Creación de las peticiones que el emisor desea enviar
    peticion1 = PeticionAlerta("Variación de temperatura de +2°C", nivel_severidad=1)
    peticion2 = PeticionAlerta("Fallo en sensor de humedad en Módulo 2", nivel_severidad=2)
    peticion3 = PeticionAlerta("Corte general del suministro eléctrico", nivel_severidad=3)
    peticion4 = PeticionAlerta("Solicitud de auditoría externa de sistema", nivel_severidad=4)

    # 4. CONCEPTO: El emisor envía la petición al primer receptor sin conocer
    # cuál de todos los objetos en la cadena terminará respondiendo.
    print("--- CASO 1: Petición Leve ---")
    monitoreo.responder_peticion(peticion1)

    print("\n--- CASO 2: Petición Media ---")
    monitoreo.responder_peticion(peticion2)

    print("\n--- CASO 3: Petición Grave ---")
    monitoreo.responder_peticion(peticion3)

    print("\n--- CASO 4: Petición Fuera de Protocolo ---")
    monitoreo.responder_peticion(peticion4)


if __name__ == "__main__":
    ejecutar_demo()