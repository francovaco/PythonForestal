from abc import ABC, abstractmethod


class Cultivo(ABC):
    """Clase abstracta base que representa un cultivo en el sistema forestal.

    Esta clase define la interfaz común para todos los tipos de cultivos
    en el sistema, incluyendo árboles y hortalizas.

    Atributos:
        _agua (int): Cantidad de agua disponible para el cultivo en litros.
        _superficie (float): Superficie que ocupa el cultivo en metros cuadrados.
    """

    def __init__(self, agua: int, superficie: float):
        """Inicializa un nuevo cultivo.

        Argumentos:
            agua (int): Cantidad inicial de agua en litros.
            superficie (float): Superficie ocupada en metros cuadrados.
        """
        self._agua = agua
        self._superficie = superficie

    def get_superficie(self) -> float:
        """Obtiene la superficie ocupada por el cultivo.

        Retorna:
            float: Superficie en metros cuadrados.
        """
        return self._superficie

    def get_agua(self) -> int:
        """Obtiene la cantidad de agua disponible del cultivo.

        Retorna:
            int: Cantidad de agua en litros.
        """
        return self._agua

    def set_agua(self, agua: int) -> None:
        """Establece la cantidad de agua del cultivo.

        Argumentos:
            agua (int): Nueva cantidad de agua en litros.
        """
        self._agua = agua