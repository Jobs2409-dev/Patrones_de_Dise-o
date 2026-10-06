# patrones_de_diseño/estructurales/adapter/main.py
from interfaces.procesador_pago import ProcesadorPago
from servicio_externo.mercado_pago_api import ServicioExternoMercadoPago
from adaptadores.adaptador_mercadopago import AdaptadorMercadoPago

def procesar_compra(pasarela: ProcesadorPago, total: float) -> None:
    """
    El cliente solo conoce 'ProcesarPago'. no tiene acoplamiento con la
    API de MercadoPago ni con sus métodos especifícos.
    """
    print(f"Iniciando checkout por un monto de ${total}")
    confirmacion = pasarela.pagar(total)
    print(confirmacion)
    
    
if __name__ == "__main__":
    print("== SISTEMA DE PAGOS: INTEGRACIÓN CON ADAPTER ==")
    
    # 1. Instanciamos la biblioteca externa incompatible
    servicio_api = ServicioExternoMercadoPago()
    
    # 2. Si intenrámos pasar 'servico_api' directo a 'procesar_compra',
    # fallaría porque no tiene el método 'pagar()'.
    # Para resolverlo, envolvemos el servico dentro del Adaptador:
    pasarela_adaptada = AdaptadorMercadoPago(servicio_api)
    
    # 3. El cliente consume el servicio externo de forma transparente
    procesar_compra(pasarela=pasarela_adaptada, total=15400.50)
