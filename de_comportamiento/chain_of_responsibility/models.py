# patrones_de_diseno/de_comportamiento/chain_of_responsibility/models.py


class PeticionAlerta:
    """
    CONCEPTO: Encapsula los datos de la petición enviada por el emisor.
    Contiene la información necesaria para que más de un objeto tenga
    la posibilidad de responder a la solicitud.
    """

    def __init__(self, descripcion: str, nivel_severidad: int):
        self.descripcion = descripcion
        self.nivel_severidad = nivel_severidad

    def __str__(self) -> str:
        return f"PeticionAlerta(Descripcion='{self.descripcion}', Severidad={self.nivel_severidad})"