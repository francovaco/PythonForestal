from .forestacion_exception import ForestacionException
from .mensajes_exception import MensajesException


class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente superficie disponible.

    Se lanza cuando se intenta plantar un cultivo que requiere más superficie
    de la que está disponible en la plantación.

    Atributos:
        _tipo_cultivo (str): Tipo de cultivo que se intentó plantar.
        _superficie_requerida (float): Superficie requerida en m².
        _superficie_disponible (float): Superficie disponible en m².
    """

    def __init__(self, tipo_cultivo: str, superficie_requerida: float, superficie_disponible: float):
        """Inicializa la excepción de superficie insuficiente.

        Argumentos:
            tipo_cultivo (str): Nombre del tipo de cultivo.
            superficie_requerida (float): Superficie requerida en metros cuadrados.
            superficie_disponible (float): Superficie disponible en metros cuadrados.
        """
        self._tipo_cultivo = tipo_cultivo
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

        message = MensajesException.get_superficie_insuficiente_message(
            tipo_cultivo, superficie_requerida, superficie_disponible
        )

        super().__init__(
            MensajesException.ERROR_CODE_SUPERFICIE_INSUFICIENTE,
            message,
            message
        )

    def get_tipo_cultivo(self) -> str:
        """Obtiene el tipo de cultivo.

        Retorna:
            str: Nombre del tipo de cultivo.
        """
        return self._tipo_cultivo

    def get_superficie_requerida(self) -> float:
        """Obtiene la superficie requerida.

        Retorna:
            float: Superficie requerida en metros cuadrados.
        """
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        """Obtiene la superficie disponible.

        Retorna:
            float: Superficie disponible en metros cuadrados.
        """
        return self._superficie_disponible