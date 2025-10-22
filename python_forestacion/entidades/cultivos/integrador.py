"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================

from .cultivo import Cultivo
from .arbol import Arbol
from .hortaliza import Hortaliza
from .pino import Pino
from .olivo import Olivo
from .lechuga import Lechuga
from .zanahoria import Zanahoria
from .tipo_aceituna import TipoAceituna

__all__ = [
    'Cultivo',
    'Arbol',
    'Hortaliza',
    'Pino',
    'Olivo',
    'Lechuga',
    'Zanahoria',
    'TipoAceituna'
]

# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

from .hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)


class Zanahoria(Hortaliza):
    """Clase que representa una zanahoria en el sistema forestal.

    Subclase de Hortaliza que representa específicamente una zanahoria con sus
    características particulares como si es una zanahoria baby o no.

    Atributos:
        _is_baby_carrot (bool): Indica si es una zanahoria baby.
    """

    def __init__(self, is_baby_carrot: bool):
        """Inicializa una nueva zanahoria.

        Argumentos:
            is_baby_carrot (bool): True si es zanahoria baby, False en caso contrario.
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._is_baby_carrot = is_baby_carrot

    def is_baby_carrot(self) -> bool:
        """Verifica si es una zanahoria baby.

        Retorna:
            bool: True si es zanahoria baby, False en caso contrario.
        """
        return self._is_baby_carrot

    def set_baby_carrot(self, is_baby: bool) -> None:
        """Establece si la zanahoria es baby.

        Argumentos:
            is_baby (bool): True para marcarla como baby, False en caso contrario.
        """
        self._is_baby_carrot = is_baby

