# patrones_de_diseño/estructurales/adapter/serivio_externo/mercado_pago_api.py
# Simula la librería externa cuya interfaz no coincide con la de 
# nuestro software.
class ServicioExternoMercadoPago:
    """
    CONCEPTO: "Interfaces que no son compatibles".
    
    Esta clase (Adaptee) representa un SDK externo o servicio legado.
    Tiene su propia lógica y método ('realizar_cobro_tarjeta'), el cual
    recibe parámetros distintos y posee una firma incompatible con 
    'ProcesadorPago'. No podemos modificar esta clase directamente.
    """
    def realizar_cobro_tarjeta(self, dinero: float, moneda: str) -> str:
        return f"[API MP] Cobro exitoso de {dinero} {moneda} procesado en pasarela externa."
    
    