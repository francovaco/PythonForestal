from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from .tierra import Tierra


class Plantacion:
    """Representa una plantación con cultivos, trabajadores y recursos.

    Una plantación es un espacio con superficie definida que contiene cultivos,
    trabajadores y agua disponible. Puede estar asociada a una tierra con
    registro catastral.

    Atributos:
        _nombre (str): Nombre identificatorio de la plantación.
        _superficie (float): Superficie total en metros cuadrados.
        _agua_disponible (int): Cantidad de agua disponible en litros.
        _cultivos (List[Cultivo]): Lista de cultivos en la plantación.
        _trabajadores (List[Trabajador]): Lista de trabajadores asignados.
        _tierra (Tierra): Tierra asociada a la plantación.
    """

    def __init__(self, nombre: str, superficie: float, agua: int):
        """Inicializa una nueva plantación.

        Argumentos:
            nombre (str): Nombre de la plantación.
            superficie (float): Superficie en metros cuadrados.
            agua (int): Cantidad inicial de agua disponible en litros.

        Raises:
            ValueError: Si el agua es negativa.
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")

        self._nombre = nombre
        self._superficie = superficie
        self._agua_disponible = agua
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []
        self._tierra = None

    def get_nombre(self) -> str:
        """Obtiene el nombre de la plantación.

        Retorna:
            str: Nombre de la plantación.
        """
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        """Establece el nombre de la plantación.

        Argumentos:
            nombre (str): Nuevo nombre.
        """
        self._nombre = nombre

    def get_superficie(self) -> float:
        """Obtiene la superficie de la plantación.

        Retorna:
            float: Superficie en metros cuadrados.
        """
        return self._superficie

    def get_agua_disponible(self) -> int:
        """Obtiene el agua disponible en la plantación.

        Retorna:
            int: Cantidad de agua en litros.
        """
        return self._agua_disponible

    def set_agua_disponible(self, agua: int) -> None:
        """Establece el agua disponible en la plantación.

        Argumentos:
            agua (int): Nueva cantidad de agua en litros.

        Raises:
            ValueError: Si el agua es negativa.
        """
        if agua < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        """Obtiene una copia de la lista de cultivos.

        Retorna:
            List[Cultivo]: Copia de la lista de cultivos.
        """
        return self._cultivos.copy()

    def get_cultivos_interno(self) -> List['Cultivo']:
        """Obtiene la lista interna de cultivos (sin copiar).

        Retorna:
            List[Cultivo]: Referencia a la lista interna de cultivos.
        """
        return self._cultivos

    def get_trabajadores(self) -> List['Trabajador']:
        """Obtiene una copia de la lista de trabajadores.

        Retorna:
            List[Trabajador]: Copia de la lista de trabajadores.
        """
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        """Establece la lista de trabajadores.

        Argumentos:
            trabajadores (List[Trabajador]): Nueva lista de trabajadores.
        """
        self._trabajadores = trabajadores.copy()

    def get_tierra(self) -> 'Tierra':
        """Obtiene la tierra asociada a la plantación.

        Retorna:
            Tierra: Tierra asociada o None si no tiene.
        """
        return self._tierra

    def set_tierra(self, tierra: 'Tierra') -> None:
        """Establece la tierra asociada a la plantación.

        Argumentos:
            tierra (Tierra): Tierra a asociar.
        """
        self._tierra = tierra