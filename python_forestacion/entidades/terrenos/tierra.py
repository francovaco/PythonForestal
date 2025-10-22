from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .plantacion import Plantacion


class Tierra:
    """Representa una tierra con registro catastral.

    Una tierra tiene identificación catastral, superficie y domicilio.
    Puede estar asociada a una plantación (finca).

    Atributos:
        _id_padron_catastral (int): Identificador del padrón catastral.
        _superficie (float): Superficie en metros cuadrados.
        _domicilio (str): Dirección o ubicación de la tierra.
        _finca (Plantacion): Plantación asociada a esta tierra.
    """

    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        """Inicializa una nueva tierra.

        Argumentos:
            id_padron_catastral (int): Identificador catastral único.
            superficie (float): Superficie en metros cuadrados.
            domicilio (str): Dirección o ubicación.

        Raises:
            ValueError: Si la superficie es menor o igual a cero.
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")

        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = None

    def get_id_padron_catastral(self) -> int:
        """Obtiene el identificador del padrón catastral.

        Retorna:
            int: ID del padrón catastral.
        """
        return self._id_padron_catastral

    def get_superficie(self) -> float:
        """Obtiene la superficie de la tierra.

        Retorna:
            float: Superficie en metros cuadrados.
        """
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """Establece la superficie de la tierra.

        Argumentos:
            superficie (float): Nueva superficie en metros cuadrados.

        Raises:
            ValueError: Si la superficie es menor o igual a cero.
        """
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def get_domicilio(self) -> str:
        """Obtiene el domicilio de la tierra.

        Retorna:
            str: Dirección o ubicación.
        """
        return self._domicilio

    def set_domicilio(self, domicilio: str) -> None:
        """Establece el domicilio de la tierra.

        Argumentos:
            domicilio (str): Nueva dirección o ubicación.
        """
        self._domicilio = domicilio

    def get_finca(self) -> 'Plantacion':
        """Obtiene la plantación asociada a esta tierra.

        Retorna:
            Plantacion: Plantación asociada o None si no tiene.
        """
        return self._finca

    def set_finca(self, finca: 'Plantacion') -> None:
        """Establece la plantación asociada a esta tierra.

        Argumentos:
            finca (Plantacion): Plantación a asociar.
        """
        self._finca = finca