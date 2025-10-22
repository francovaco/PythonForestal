from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tierra import Tierra
    from .plantacion import Plantacion


class RegistroForestal:
    """Representa un registro forestal que vincula tierra y plantación.

    El registro forestal mantiene información catastral, administrativa y
    económica de una propiedad forestal.

    Atributos:
        _id_padron (int): Identificador del padrón.
        _tierra (Tierra): Tierra registrada.
        _plantacion (Plantacion): Plantación en la tierra.
        _propietario (str): Nombre del propietario.
        _avaluo (float): Valor catastral o avalúo fiscal.
    """

    def __init__(self, id_padron: int, tierra: 'Tierra', plantacion: 'Plantacion',
                 propietario: str, avaluo: float):
        """Inicializa un nuevo registro forestal.

        Argumentos:
            id_padron (int): Identificador del padrón.
            tierra (Tierra): Tierra a registrar.
            plantacion (Plantacion): Plantación asociada.
            propietario (str): Nombre del propietario.
            avaluo (float): Valor catastral.
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        """Obtiene el identificador del padrón.

        Retorna:
            int: ID del padrón.
        """
        return self._id_padron

    def get_tierra(self) -> 'Tierra':
        """Obtiene la tierra registrada.

        Retorna:
            Tierra: Tierra del registro.
        """
        return self._tierra

    def get_plantacion(self) -> 'Plantacion':
        """Obtiene la plantación registrada.

        Retorna:
            Plantacion: Plantación del registro.
        """
        return self._plantacion

    def get_propietario(self) -> str:
        """Obtiene el nombre del propietario.

        Retorna:
            str: Nombre del propietario.
        """
        return self._propietario

    def get_avaluo(self) -> float:
        """Obtiene el avalúo fiscal de la propiedad.

        Retorna:
            float: Valor catastral.
        """
        return self._avaluo