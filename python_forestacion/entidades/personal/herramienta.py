class Herramienta:
    """Representa una herramienta de trabajo utilizada por los trabajadores.

    Cada herramienta tiene un identificador único, nombre y un indicador
    de si requiere certificado de higiene y seguridad para su uso.

    Atributos:
        _id (int): Identificador único de la herramienta.
        _nombre (str): Nombre descriptivo de la herramienta.
        _certificado_hys (bool): Indica si requiere certificado de higiene y seguridad.
    """

    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool):
        """Inicializa una nueva herramienta.

        Argumentos:
            id_herramienta (int): Identificador único de la herramienta.
            nombre (str): Nombre de la herramienta (ej: "Pala", "Motosierra").
            certificado_hys (bool): True si requiere certificado de higiene y seguridad,
                False en caso contrario.
        """
        self._id = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_id(self) -> int:
        """Obtiene el identificador único de la herramienta.

        Retorna:
            int: ID de la herramienta.
        """
        return self._id

    def get_nombre(self) -> str:
        """Obtiene el nombre de la herramienta.

        Retorna:
            str: Nombre descriptivo de la herramienta.
        """
        return self._nombre

    def get_certificado_hys(self) -> bool:
        """Verifica si la herramienta requiere certificado de higiene y seguridad.

        Retorna:
            bool: True si requiere certificado HyS, False en caso contrario.
        """
        return self._certificado_hys