from .hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA
)


class Lechuga(Hortaliza):
    """Clase que representa una lechuga en el sistema forestal.

    Subclase de Hortaliza que representa específicamente una lechuga con sus
    características particulares como la variedad. Las lechugas requieren
    invernadero para su cultivo.

    Atributos:
        _variedad (str): Variedad específica de la lechuga (ej: "Crespa", "Mantecosa").
    """

    def __init__(self, variedad: str):
        """Inicializa una nueva lechuga.

        Argumentos:
            variedad (str): Variedad de la lechuga.
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Obtiene la variedad de la lechuga.

        Retorna:
            str: Nombre de la variedad de la lechuga.
        """
        return self._variedad