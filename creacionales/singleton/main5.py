# singleton/main.py
from configuracion import Configuracion


if __name__ == "__main__":
    print("=== PASO 1: OBTENER PRIMERA INSTANCIA ===")
    config1 = Configuracion()
    print(f"config1 -> {config1.obtener_estado()}")

    print("\n=== PASO 2: MODIFICAR ESTADO DESDE LA PRIMERA REFERENCIA ===")
    config1.actualizar_parametros(idioma="EN", modo_oscuro=True)
    print(f"config1 modificado -> {config1.obtener_estado()}")

    print("\n=== PASO 3: INTENTAR CREAR UNA 'SEGUNDA' INSTANCIA ===")
    # CONCEPTO: "Restringe la creación... a un único objeto"
    # El cliente invoca el constructor habitual, pero el patrón retorna el objeto existente.
    config2 = Configuracion()
    print(f"config2 obtenido   -> {config2.obtener_estado()}")

    print("\n=== PASO 4: VERIFICACIÓN FORMAL DE IDENTIDAD (is y id) ===")
    son_identicos = config1 is config2
    print(f"¿Son exactamente el mismo objeto en memoria? {son_identicos}")
    print(f"Dirección de memoria config1: {hex(id(config1))}")
    print(f"Dirección de memoria config2: {hex(id(config2))}")