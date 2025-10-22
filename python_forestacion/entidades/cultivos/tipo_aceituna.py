from enum import Enum, auto


class TipoAceituna(Enum):
    """Enumeración de los tipos de aceitunas disponibles.

    Define los diferentes tipos de aceitunas que pueden producir los olivos
    en el sistema forestal.

    Atributos:
        ARBEQUINA: Variedad de aceituna Arbequina.
        PICUAL: Variedad de aceituna Picual.
        MANZANILLA: Variedad de aceituna Manzanilla.
    """

    ARBEQUINA = auto()
    PICUAL = auto()
    MANZANILLA = auto()