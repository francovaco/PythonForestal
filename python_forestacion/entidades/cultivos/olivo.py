from .arbol import Arbol
from .tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    ALTURA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO
)


class Olivo(Arbol):
    """Clase que representa un olivo en el sistema forestal.

    Subclase de Arbol que representa específicamente un olivo con sus
    características particulares como el tipo de aceituna que produce.

    Atributos:
        _tipo (TipoAceituna): Tipo de aceituna que produce el olivo.
    """

    def __init__(self, tipo: TipoAceituna):
        """Inicializa un nuevo olivo.

        Argumentos:
            tipo (TipoAceituna): Tipo de aceituna del olivo.
        """
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            altura=ALTURA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO
        )
        self._tipo = tipo

    def get_tipo(self) -> TipoAceituna:
        """Obtiene el tipo de aceituna del olivo.

        Retorna:
            TipoAceituna: Tipo de aceituna que produce.
        """
        return self._tipo