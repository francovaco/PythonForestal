from .hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)


class Zanahoria(Hortaliza):
    """Clase que representa una zanahoria en el sistema forestal.

    Subclase de Hortaliza que representa específicamente una zanahoria con sus
    características particulares como si es una zanahoria baby o no.

    Atributos:
        _is_baby_carrot (bool): Indica si es una zanahoria baby.
    """

    def __init__(self, is_baby_carrot: bool):
        """Inicializa una nueva zanahoria.

        Argumentos:
            is_baby_carrot (bool): True si es zanahoria baby, False en caso contrario.
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._is_baby_carrot = is_baby_carrot

    def is_baby_carrot(self) -> bool:
        """Verifica si es una zanahoria baby.

        Retorna:
            bool: True si es zanahoria baby, False en caso contrario.
        """
        return self._is_baby_carrot

    def set_baby_carrot(self, is_baby: bool) -> None:
        """Establece si la zanahoria es baby.

        Argumentos:
            is_baby (bool): True para marcarla como baby, False en caso contrario.
        """
        self._is_baby_carrot = is_baby