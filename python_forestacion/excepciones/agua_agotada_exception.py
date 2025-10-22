from .forestacion_exception import ForestacionException
from .mensajes_exception import MensajesException


class AguaAgotadaException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente agua disponible.

    Se lanza cuando se intenta realizar una operación que requiere una cantidad
    mínima de agua y la plantación no tiene suficiente agua disponible.

    Atributos:
        _agua_disponible (int): Cantidad de agua disponible en litros.
        _agua_minima (int): Cantidad mínima de agua requerida en litros.
    """

    def __init__(self, agua_disponible: int, agua_minima: int):
        """Inicializa la excepción de agua agotada.

        Argumentos:
            agua_disponible (int): Agua disponible actual en litros.
            agua_minima (int): Agua mínima requerida en litros.
        """
        self._agua_disponible = agua_disponible
        self._agua_minima = agua_minima

        message = MensajesException.get_agua_agotada_message(agua_disponible, agua_minima)

        super().__init__(
            MensajesException.ERROR_CODE_AGUA_AGOTADA,
            message,
            message
        )

    def get_agua_disponible(self) -> int:
        """Obtiene la cantidad de agua disponible.

        Retorna:
            int: Agua disponible en litros.
        """
        return self._agua_disponible

    def get_agua_minima(self) -> int:
        """Obtiene la cantidad mínima de agua requerida.

        Retorna:
            int: Agua mínima en litros.
        """
        return self._agua_minima