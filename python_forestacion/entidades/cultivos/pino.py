from .arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    ALTURA_INICIAL_ARBOL,
    SUPERFICIE_PINO
)


class Pino(Arbol):
    """Clase que representa un pino en el sistema forestal.

    Subclase de Arbol que representa específicamente un pino con sus
    características particulares como la variedad.

    Atributos:
        _variedad (str): Variedad específica del pino (ej: "Parana").
    """

    def __init__(self, variedad: str):
        """Inicializa un nuevo pino.

        Argumentos:
            variedad (str): Variedad del pino.
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            altura=ALTURA_INICIAL_ARBOL,
            superficie=SUPERFICIE_PINO
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Obtiene la variedad del pino.

        Retorna:
            str: Nombre de la variedad del pino.
        """
        return self._variedad