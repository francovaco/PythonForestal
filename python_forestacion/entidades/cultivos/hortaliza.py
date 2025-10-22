from .cultivo import Cultivo


class Hortaliza(Cultivo):
    """Clase que representa una hortaliza en el sistema forestal.

    Extiende la clase Cultivo agregando características específicas de hortalizas
    como la indicación de si requiere invernadero.

    Atributos:
        _invernadero (bool): Indica si la hortaliza requiere invernadero.
    """

    def __init__(self, agua: int, superficie: float, invernadero: bool):
        """Inicializa una nueva hortaliza.

        Argumentos:
            agua (int): Cantidad inicial de agua en litros.
            superficie (float): Superficie ocupada en metros cuadrados.
            invernadero (bool): True si requiere invernadero, False en caso contrario.
        """
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def get_invernadero(self) -> bool:
        """Obtiene si la hortaliza requiere invernadero.

        Retorna:
            bool: True si requiere invernadero, False en caso contrario.
        """
        return self._invernadero