# patrones_de_diseño/estructurales/adapter/adaptadores/adaptador_mercadopago.py
from interfaces.procesador_pago import ProcesadorPago
from servicio_externo.mercado_pago_api import ServicioExternoMercadoPago

class AdaptadorMercadoPago(ProcesadorPago):
    """
    CONCEPTO:
    1)_ "Se utiliza para vincular dos interfaces que no son compatibles
        y utiliza sus funcionalidades".
    2)_ "El adaptador permite que las clases trabajen juntas de otra 
        manera que no podrían".
    3)_ "Forma de componer objetos para obtener nuevas funcionalidades".
    
    El adpatador:
    - Hereda de 'ProcesadorPago' (cumple el contrato que el cliente espera).
    - Contiene por composición un instancia de 'ServicioExternoMercadoPago'.
    """
    def __init__(self, servicio_externo: ServicioExternoMercadoPago):
        # Composición de estructura de objetos
        self._servicio_externo = servicio_externo
        
    def pagar(self, monto: float) -> str:
        # Traduce la llamada estándar 'pagar(monto)' al método
        # incompatible 'realizar_cobro_tarjeta(dinero, moneda)'.
        moneda_default = "ARS"
        resultado = self._servicio_externo.realizar_cobro_tarjeta(dinero=monto, moneda=moneda_default)
        return f"Adaptador -> {resultado}"