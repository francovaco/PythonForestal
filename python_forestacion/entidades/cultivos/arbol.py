from .cultivo import Cultivo
import threading


class Arbol(Cultivo):
    """Clase que representa un árbol en el sistema forestal.

    Extiende la clase Cultivo agregando características específicas de árboles
    como altura. Implementa un contador thread-safe para asignar IDs únicos.

    Atributos:
        _altura (float): Altura del árbol en metros.
        _id (int): Identificador único del árbol.
        _contador (int): Contador de clase para generar IDs únicos.
        _lock (threading.Lock): Lock para garantizar thread-safety del contador.
    """

    _contador = 0
    _lock = threading.Lock()

    def __init__(self, agua: int, altura: float, superficie: float):
        """Inicializa un nuevo árbol.

        Argumentos:
            agua (int): Cantidad inicial de agua en litros.
            altura (float): Altura inicial del árbol en metros.
            superficie (float): Superficie ocupada en metros cuadrados.
        """
        super().__init__(agua, superficie)
        self._altura = altura

        with Arbol._lock:
            Arbol._contador += 1
            self._id = Arbol._contador

    def get_id(self) -> int:
        """Obtiene el identificador único del árbol.

        Retorna:
            int: ID único del árbol.
        """
        return self._id

    def get_altura(self) -> float:
        """Obtiene la altura del árbol.

        Retorna:
            float: Altura en metros.
        """
        return self._altura

    def set_altura(self, altura: float) -> None:
        """Establece la altura del árbol.

        Argumentos:
            altura (float): Nueva altura en metros.
        """
        self._altura = altura