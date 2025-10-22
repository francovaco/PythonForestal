"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion
Fecha de generacion: 2025-10-21 21:15:59
Total de archivos integrados: 66
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades/cultivos
#   4. __init__.py
#   5. arbol.py
#   6. cultivo.py
#   7. hortaliza.py
#   8. lechuga.py
#   9. olivo.py
#   10. pino.py
#   11. tipo_aceituna.py
#   12. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   13. __init__.py
#   14. apto_medico.py
#   15. herramienta.py
#   16. tarea.py
#   17. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   18. __init__.py
#   19. plantacion.py
#   20. registro_forestal.py
#   21. tierra.py
#
# DIRECTORIO: excepciones
#   22. __init__.py
#   23. agua_agotada_exception.py
#   24. forestacion_exception.py
#   25. mensajes_exception.py
#   26. persistencia_exception.py
#   27. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   28. __init__.py
#
# DIRECTORIO: patrones/factory
#   29. __init__.py
#   30. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   31. __init__.py
#   32. observable.py
#   33. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   34. __init__.py
#   35. evento_plantacion.py
#   36. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#   37. __init__.py
#
# DIRECTORIO: patrones/strategy
#   38. __init__.py
#   39. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   40. __init__.py
#   41. absorcion_constante_strategy.py
#   42. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   43. __init__.py
#
# DIRECTORIO: riego/control
#   44. __init__.py
#   45. control_riego_task.py
#
# DIRECTORIO: riego/sensores
#   46. __init__.py
#   47. humedad_reader_task.py
#   48. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   49. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   50. __init__.py
#   51. arbol_service.py
#   52. cultivo_service.py
#   53. cultivo_service_registry.py
#   54. lechuga_service.py
#   55. olivo_service.py
#   56. pino_service.py
#   57. zanahoria_service.py
#
# DIRECTORIO: servicios/negocio
#   58. __init__.py
#   59. fincas_service.py
#   60. paquete.py
#
# DIRECTORIO: servicios/personal
#   61. __init__.py
#   62. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   63. __init__.py
#   64. plantacion_service.py
#   65. registro_forestal_service.py
#   66. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/66: __init__.py
# Directorio: .
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/66: constantes.py
# Directorio: .
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/constantes.py
# ==============================================================================

"""Constantes de configuración del sistema de gestión forestal.

Este módulo centraliza todas las constantes utilizadas en el sistema,
incluyendo parámetros de cultivos, riego, sensores y persistencia.

Atributos:
    AGUA_MINIMA (int): Cantidad mínima de agua requerida en la plantación en litros.
    AGUA_INICIAL_PLANTACION (int): Agua inicial al crear una plantación en litros.

    TEMP_MIN_RIEGO (int): Temperatura mínima para activar riego en °C.
    TEMP_MAX_RIEGO (int): Temperatura máxima para activar riego en °C.
    HUMEDAD_MAX_RIEGO (int): Humedad máxima para activar riego en %.

    SUPERFICIE_PINO (float): Superficie requerida por pino en m².
    SUPERFICIE_OLIVO (float): Superficie requerida por olivo en m².
    SUPERFICIE_LECHUGA (float): Superficie requerida por lechuga en m².
    SUPERFICIE_ZANAHORIA (float): Superficie requerida por zanahoria en m².

    AGUA_INICIAL_PINO (int): Agua inicial de un pino en litros.
    AGUA_INICIAL_OLIVO (int): Agua inicial de un olivo en litros.
    AGUA_INICIAL_LECHUGA (int): Agua inicial de una lechuga en litros.
    AGUA_INICIAL_ZANAHORIA (int): Agua inicial de una zanahoria en litros.

    ALTURA_INICIAL_ARBOL (float): Altura inicial de árboles genéricos en metros.
    ALTURA_INICIAL_OLIVO (float): Altura inicial de olivos en metros.

    ABSORCION_SEASONAL_VERANO (int): Absorción de agua en verano en litros.
    ABSORCION_SEASONAL_INVIERNO (int): Absorción de agua en invierno en litros.
    ABSORCION_CONSTANTE_LECHUGA (int): Absorción constante de lechuga en litros.
    ABSORCION_CONSTANTE_ZANAHORIA (int): Absorción constante de zanahoria en litros.

    MES_INICIO_VERANO (int): Mes de inicio del verano (1-12).
    MES_FIN_VERANO (int): Mes de fin del verano (1-12).

    CRECIMIENTO_PINO_POR_RIEGO (float): Incremento de altura del pino por riego en metros.
    CRECIMIENTO_OLIVO_POR_RIEGO (float): Incremento de altura del olivo por riego en metros.

    INTERVALO_SENSOR_TEMPERATURA (float): Intervalo de lectura del sensor en segundos.
    INTERVALO_SENSOR_HUMEDAD (float): Intervalo de lectura del sensor en segundos.
    INTERVALO_CONTROL_RIEGO (float): Intervalo de evaluación del control en segundos.
    THREAD_JOIN_TIMEOUT (float): Timeout para join de threads en segundos.

    SENSOR_TEMP_MIN (int): Temperatura mínima del sensor en °C.
    SENSOR_TEMP_MAX (int): Temperatura máxima del sensor en °C.
    SENSOR_HUMEDAD_MIN (int): Humedad mínima del sensor en %.
    SENSOR_HUMEDAD_MAX (int): Humedad máxima del sensor en %.

    DIRECTORIO_DATA (str): Directorio para archivos de persistencia.
    EXTENSION_DATA (str): Extensión de archivos de datos.
"""

AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50

SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 3.0
SUPERFICIE_LECHUGA = 0.10
SUPERFICIE_ZANAHORIA = 0.15

AGUA_INICIAL_PINO = 2
AGUA_INICIAL_OLIVO = 5
AGUA_INICIAL_LECHUGA = 1
AGUA_INICIAL_ZANAHORIA = 0

ALTURA_INICIAL_ARBOL = 1.0
ALTURA_INICIAL_OLIVO = 0.5

ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
ABSORCION_CONSTANTE_LECHUGA = 1
ABSORCION_CONSTANTE_ZANAHORIA = 2

MES_INICIO_VERANO = 3
MES_FIN_VERANO = 8

CRECIMIENTO_PINO_POR_RIEGO = 0.10
CRECIMIENTO_OLIVO_POR_RIEGO = 0.01

INTERVALO_SENSOR_TEMPERATURA = 2.0
INTERVALO_SENSOR_HUMEDAD = 3.0
INTERVALO_CONTROL_RIEGO = 2.5
THREAD_JOIN_TIMEOUT = 2.0

SENSOR_TEMP_MIN = -25
SENSOR_TEMP_MAX = 50
SENSOR_HUMEDAD_MIN = 0
SENSOR_HUMEDAD_MAX = 100

DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/66: __init__.py
# Directorio: entidades
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 4/66: __init__.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 5/66: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 6/66: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 7/66: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 8/66: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 9/66: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 10/66: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 11/66: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 12/66: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 13/66: __init__.py
# Directorio: entidades/personal
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal/__init__.py
# ==============================================================================

from .trabajador import Trabajador
from .herramienta import Herramienta
from .tarea import Tarea
from .apto_medico import AptoMedico

__all__ = [
    'Trabajador',
    'Herramienta',
    'Tarea',
    'AptoMedico'
]

# ==============================================================================
# ARCHIVO 14/66: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

from datetime import date


class AptoMedico:
    """Representa el certificado de aptitud médica de un trabajador.

    Contiene información sobre el estado de salud del trabajador, la fecha
    de emisión del certificado y observaciones médicas relevantes.

    Atributos:
        _apto (bool): Indica si el trabajador está apto para trabajar.
        _fecha_emision (date): Fecha de emisión del certificado médico.
        _observaciones (str): Observaciones o notas adicionales del médico.
    """

    def __init__(self, apto: bool, fecha_emision: date, observaciones: str):
        """Inicializa un nuevo certificado de apto médico.

        Argumentos:
            apto (bool): True si el trabajador está apto, False en caso contrario.
            fecha_emision (date): Fecha de emisión del certificado.
            observaciones (str): Observaciones médicas o notas adicionales.
        """
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def esta_apto(self) -> bool:
        """Verifica si el trabajador está apto para trabajar.

        Retorna:
            bool: True si está apto médicamente, False en caso contrario.
        """
        return self._apto

    def set_apto(self, apto: bool) -> None:
        """Establece el estado de aptitud médica del trabajador.

        Argumentos:
            apto (bool): True para marcar como apto, False para no apto.
        """
        self._apto = apto

    def get_fecha_emision(self) -> date:
        """Obtiene la fecha de emisión del certificado médico.

        Retorna:
            date: Fecha en que se emitió el certificado.
        """
        return self._fecha_emision

    def get_observaciones(self) -> str:
        """Obtiene las observaciones médicas del certificado.

        Retorna:
            str: Observaciones o notas del médico sobre el estado del trabajador.
        """
        return self._observaciones

# ==============================================================================
# ARCHIVO 15/66: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

class Herramienta:
    """Representa una herramienta de trabajo utilizada por los trabajadores.

    Cada herramienta tiene un identificador único, nombre y un indicador
    de si requiere certificado de higiene y seguridad para su uso.

    Atributos:
        _id (int): Identificador único de la herramienta.
        _nombre (str): Nombre descriptivo de la herramienta.
        _certificado_hys (bool): Indica si requiere certificado de higiene y seguridad.
    """

    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool):
        """Inicializa una nueva herramienta.

        Argumentos:
            id_herramienta (int): Identificador único de la herramienta.
            nombre (str): Nombre de la herramienta (ej: "Pala", "Motosierra").
            certificado_hys (bool): True si requiere certificado de higiene y seguridad,
                False en caso contrario.
        """
        self._id = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_id(self) -> int:
        """Obtiene el identificador único de la herramienta.

        Retorna:
            int: ID de la herramienta.
        """
        return self._id

    def get_nombre(self) -> str:
        """Obtiene el nombre de la herramienta.

        Retorna:
            str: Nombre descriptivo de la herramienta.
        """
        return self._nombre

    def get_certificado_hys(self) -> bool:
        """Verifica si la herramienta requiere certificado de higiene y seguridad.

        Retorna:
            bool: True si requiere certificado HyS, False en caso contrario.
        """
        return self._certificado_hys

# ==============================================================================
# ARCHIVO 16/66: tarea.py
# Directorio: entidades/personal
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

from datetime import date


class Tarea:
    """Representa una tarea asignada a un trabajador.

    Una tarea tiene un identificador único, fecha de asignación, descripción
    y un estado que indica si fue completada o no.

    Atributos:
        _id (int): Identificador único de la tarea.
        _fecha (date): Fecha de asignación de la tarea.
        _descripcion (str): Descripción detallada de la tarea a realizar.
        _estado (bool): Estado de completitud de la tarea (False: pendiente, True: completada).
    """

    def __init__(self, id_tarea: int, fecha: date, descripcion: str):
        """Inicializa una nueva tarea.

        La tarea se crea con estado False (pendiente) por defecto.

        Argumentos:
            id_tarea (int): Identificador único de la tarea.
            fecha (date): Fecha de asignación de la tarea.
            descripcion (str): Descripción de la tarea (ej: "Desmalezar", "Abonar").
        """
        self._id = id_tarea
        self._fecha = fecha
        self._descripcion = descripcion
        self._estado = False

    def get_id(self) -> int:
        """Obtiene el identificador único de la tarea.

        Retorna:
            int: ID de la tarea.
        """
        return self._id

    def get_fecha(self) -> date:
        """Obtiene la fecha de asignación de la tarea.

        Retorna:
            date: Fecha en que se asignó la tarea.
        """
        return self._fecha

    def get_descripcion(self) -> str:
        """Obtiene la descripción de la tarea.

        Retorna:
            str: Descripción detallada de lo que debe realizarse.
        """
        return self._descripcion

    def get_estado(self) -> bool:
        """Obtiene el estado de completitud de la tarea.

        Retorna:
            bool: False si la tarea está pendiente, True si está completada.
        """
        return self._estado

    def set_estado(self, estado: bool) -> None:
        """Establece el estado de completitud de la tarea.

        Argumentos:
            estado (bool): True para marcar como completada, False para pendiente.
        """
        self._estado = estado

# ==============================================================================
# ARCHIVO 17/66: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

from typing import List
from datetime import date
from .apto_medico import AptoMedico
from .tarea import Tarea


class Trabajador:
    """Representa un trabajador en el sistema de gestión forestal.

    Un trabajador tiene identificación personal, tareas asignadas y un
    certificado de apto médico. Se crea con un apto médico por defecto
    indicando que no tiene certificado.

    Atributos:
        _dni (int): Documento Nacional de Identidad del trabajador.
        _nombre (str): Nombre completo del trabajador.
        _tareas (List[Tarea]): Lista de tareas asignadas al trabajador.
        _apto_medico (AptoMedico): Certificado de aptitud médica del trabajador.
    """

    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        """Inicializa un nuevo trabajador.

        El trabajador se crea con un apto médico por defecto que indica
        "Sin certificado" y estado no apto (False).

        Argumentos:
            dni (int): Documento Nacional de Identidad del trabajador.
            nombre (str): Nombre completo del trabajador.
            tareas (List[Tarea]): Lista de tareas asignadas. Se crea una copia
                para evitar efectos colaterales.
        """
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas.copy()
        self._apto_medico = AptoMedico(False, date.today(), "Sin certificado")

    def get_dni(self) -> int:
        """Obtiene el DNI del trabajador.

        Retorna:
            int: Documento Nacional de Identidad.
        """
        return self._dni

    def get_nombre(self) -> str:
        """Obtiene el nombre del trabajador.

        Retorna:
            str: Nombre completo del trabajador.
        """
        return self._nombre

    def get_tareas(self) -> List[Tarea]:
        """Obtiene una copia de la lista de tareas del trabajador.

        Retorna una copia para evitar modificaciones externas de la lista interna.

        Retorna
            List[Tarea]: Copia de la lista de tareas asignadas.
        """
        return self._tareas.copy()

    def get_apto_medico(self) -> AptoMedico:
        """Obtiene el certificado de apto médico del trabajador.

        Retorna:
            AptoMedico: Certificado de aptitud médica actual.
        """
        return self._apto_medico

    def set_apto_medico(self, apto_medico: AptoMedico) -> None:
        """Establece o actualiza el certificado de apto médico del trabajador.

        Argumentos:
            apto_medico (AptoMedico): Nuevo certificado de aptitud médica.
        """
        self._apto_medico = apto_medico


################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 18/66: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================

from .tierra import Tierra
from .plantacion import Plantacion
from .registro_forestal import RegistroForestal

__all__ = [
    'Tierra',
    'Plantacion',
    'RegistroForestal'
]

# ==============================================================================
# ARCHIVO 19/66: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 20/66: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 21/66: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 22/66: __init__.py
# Directorio: excepciones
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/__init__.py
# ==============================================================================

from .forestacion_exception import ForestacionException
from .superficie_insuficiente_exception import SuperficieInsuficienteException
from .agua_agotada_exception import AguaAgotadaException
from .persistencia_exception import PersistenciaException
from .mensajes_exception import MensajesException

__all__ = [
    'ForestacionException',
    'SuperficieInsuficienteException',
    'AguaAgotadaException',
    'PersistenciaException',
    'MensajesException'
]

# ==============================================================================
# ARCHIVO 23/66: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

from .forestacion_exception import ForestacionException
from .mensajes_exception import MensajesException


class AguaAgotadaException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente agua disponible.

    Se lanza cuando se intenta realizar una operación que requiere una cantidad
    mínima de agua y la plantación no tiene suficiente agua disponible.

    Atributos:
        _agua_disponible (int): Cantidad de agua disponible en litros.
        _agua_minima (int): Cantidad mínima de agua requerida en litros.
    """

    def __init__(self, agua_disponible: int, agua_minima: int):
        """Inicializa la excepción de agua agotada.

        Argumentos:
            agua_disponible (int): Agua disponible actual en litros.
            agua_minima (int): Agua mínima requerida en litros.
        """
        self._agua_disponible = agua_disponible
        self._agua_minima = agua_minima

        message = MensajesException.get_agua_agotada_message(agua_disponible, agua_minima)

        super().__init__(
            MensajesException.ERROR_CODE_AGUA_AGOTADA,
            message,
            message
        )

    def get_agua_disponible(self) -> int:
        """Obtiene la cantidad de agua disponible.

        Retorna:
            int: Agua disponible en litros.
        """
        return self._agua_disponible

    def get_agua_minima(self) -> int:
        """Obtiene la cantidad mínima de agua requerida.

        Retorna:
            int: Agua mínima en litros.
        """
        return self._agua_minima

# ==============================================================================
# ARCHIVO 24/66: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

class ForestacionException(Exception):
    """Excepción base para el sistema de forestación.

    Proporciona una estructura común para todas las excepciones del sistema,
    incluyendo código de error y mensajes para usuarios y desarrolladores.

    Atributos:
        _error_code (str): Código identificador del error.
        _user_message (str): Mensaje amigable para mostrar al usuario.
    """

    def __init__(self, error_code: str, message: str, user_message: str = None):
        """Inicializa una excepción de forestación.

        Argumentos:
            error_code (str): Código identificador del error.
            message (str): Mensaje técnico de la excepción.
            user_message (str, optional): Mensaje para el usuario. Si es None,
                usa el mensaje técnico.
        """
        super().__init__(message)
        self._error_code = error_code
        self._user_message = user_message if user_message else message

    def get_error_code(self) -> str:
        """Obtiene el código de error.

        Retorna:
            str: Código del error.
        """
        return self._error_code

    def get_user_message(self) -> str:
        """Obtiene el mensaje para el usuario.

        Retorna:
            str: Mensaje amigable para mostrar al usuario.
        """
        return self._user_message

    def get_full_message(self) -> str:
        """Obtiene el mensaje completo con código y descripción.

        Retorna:
            str: Mensaje formateado con código y descripción.
        """
        return f"{self._error_code} - {self._user_message}"

# ==============================================================================
# ARCHIVO 25/66: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================

class MensajesException:
    """Clase utilitaria para gestión de mensajes de excepciones.

    Proporciona constantes y métodos estáticos para generar mensajes
    consistentes en todo el sistema de excepciones.

    Esta clase no debe ser instanciada, solo usar sus métodos estáticos.

    Atributos:
        ERROR_CODE_SUPERFICIE_INSUFICIENTE (str): Código para error de superficie.
        ERROR_CODE_AGUA_AGOTADA (str): Código para error de agua agotada.
        ERROR_CODE_PERSISTENCIA (str): Código para error de persistencia.
        MSG_SUPERFICIE_INSUFICIENTE (str): Mensaje base para superficie insuficiente.
        MSG_AGUA_AGOTADA (str): Mensaje base para agua agotada.
        MSG_PERSISTENCIA_ESCRITURA (str): Mensaje para error de escritura.
        MSG_PERSISTENCIA_LECTURA (str): Mensaje para error de lectura.
    """

    ERROR_CODE_SUPERFICIE_INSUFICIENTE = "ERROR 01"
    ERROR_CODE_AGUA_AGOTADA = "ERROR 02"
    ERROR_CODE_PERSISTENCIA = "ERROR 03"

    MSG_SUPERFICIE_INSUFICIENTE = "Superficie insuficiente para plantar"
    MSG_AGUA_AGOTADA = "Agua agotada en la plantacion"
    MSG_PERSISTENCIA_ESCRITURA = "Error al persistir registro"
    MSG_PERSISTENCIA_LECTURA = "Error al leer registro"

    @staticmethod
    def get_superficie_insuficiente_message(tipo_cultivo: str, requerida: float, disponible: float) -> str:
        """Genera mensaje formateado para error de superficie insuficiente.

        Argumentos:
            tipo_cultivo (str): Tipo de cultivo que se intentó plantar.
            requerida (float): Superficie requerida en metros cuadrados.
            disponible (float): Superficie disponible en metros cuadrados.

        Retorna:
            str: Mensaje formateado con los valores.
        """
        return f"No se puede plantar {tipo_cultivo}. Requiere: {requerida:.2f} m², Disponible: {disponible:.2f} m²"

    @staticmethod
    def get_agua_agotada_message(disponible: int, minima: int) -> str:
        """Genera mensaje formateado para error de agua agotada.

        Argumentos:
            disponible (int): Agua disponible en litros.
            minima (int): Agua mínima requerida en litros.

        Retorna:
            str: Mensaje formateado con los valores.
        """
        return f"Agua insuficiente. Disponible: {disponible}L, Minimo requerido: {minima}L"

    def __init__(self):
        """Constructor privado que previene la instanciación.

        Raises:
            AssertionError: Siempre, para prevenir la instanciación.
        """
        raise AssertionError("Esta clase no debe ser instanciada")

# ==============================================================================
# ARCHIVO 26/66: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

from .forestacion_exception import ForestacionException
from .mensajes_exception import MensajesException


class PersistenciaException(ForestacionException):
    """Excepción lanzada cuando ocurre un error de persistencia.

    Se lanza cuando hay problemas al guardar o leer datos desde el
    sistema de archivos.

    Atributos:
        _nombre_archivo (str): Nombre del archivo que causó el error.
    """

    def __init__(self, message: str, nombre_archivo: str):
        """Inicializa la excepción de persistencia.

        Argumentos:
            message (str): Mensaje descriptivo del error.
            nombre_archivo (str): Nombre del archivo involucrado.
        """
        self._nombre_archivo = nombre_archivo

        super().__init__(
            MensajesException.ERROR_CODE_PERSISTENCIA,
            message,
            message
        )

    def get_nombre_archivo(self) -> str:
        """Obtiene el nombre del archivo que causó el error.

        Retorna:
            str: Nombre del archivo.
        """
        return self._nombre_archivo

# ==============================================================================
# ARCHIVO 27/66: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

from .forestacion_exception import ForestacionException
from .mensajes_exception import MensajesException


class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando no hay suficiente superficie disponible.

    Se lanza cuando se intenta plantar un cultivo que requiere más superficie
    de la que está disponible en la plantación.

    Atributos:
        _tipo_cultivo (str): Tipo de cultivo que se intentó plantar.
        _superficie_requerida (float): Superficie requerida en m².
        _superficie_disponible (float): Superficie disponible en m².
    """

    def __init__(self, tipo_cultivo: str, superficie_requerida: float, superficie_disponible: float):
        """Inicializa la excepción de superficie insuficiente.

        Argumentos:
            tipo_cultivo (str): Nombre del tipo de cultivo.
            superficie_requerida (float): Superficie requerida en metros cuadrados.
            superficie_disponible (float): Superficie disponible en metros cuadrados.
        """
        self._tipo_cultivo = tipo_cultivo
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

        message = MensajesException.get_superficie_insuficiente_message(
            tipo_cultivo, superficie_requerida, superficie_disponible
        )

        super().__init__(
            MensajesException.ERROR_CODE_SUPERFICIE_INSUFICIENTE,
            message,
            message
        )

    def get_tipo_cultivo(self) -> str:
        """Obtiene el tipo de cultivo.

        Retorna:
            str: Nombre del tipo de cultivo.
        """
        return self._tipo_cultivo

    def get_superficie_requerida(self) -> float:
        """Obtiene la superficie requerida.

        Retorna:
            float: Superficie requerida en metros cuadrados.
        """
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        """Obtiene la superficie disponible.

        Retorna:
            float: Superficie disponible en metros cuadrados.
        """
        return self._superficie_disponible


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 28/66: __init__.py
# Directorio: patrones
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 29/66: __init__.py
# Directorio: patrones/factory
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/factory/__init__.py
# ==============================================================================

from .cultivo_factory import CultivoFactory

__all__ = [
    'CultivoFactory'
]

# ==============================================================================
# ARCHIVO 30/66: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """Fábrica para la creación de instancias de cultivos.

    Implementa el patrón Factory Method para desacoplar la creación de objetos
    de cultivo del código cliente. Permite crear diferentes tipos de cultivos
    sin que el cliente conozca las clases concretas.

    Este patrón facilita la extensibilidad del sistema al agregar nuevos tipos
    de cultivos sin modificar el código existente.
    """

    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """Crea una instancia de cultivo según la especie especificada.

        Argumentos:
            especie (str): Nombre de la especie del cultivo a crear.
                Valores válidos: "Pino", "Olivo", "Lechuga", "Zanahoria".

        Retorna:
            Cultivo: Instancia del tipo de cultivo solicitado.

        Raises:
            ValueError: Si la especie especificada no está registrada en la fábrica.
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> 'Cultivo':
        """Crea una instancia de Pino con configuración por defecto.

        Retorna:
            Cultivo: Instancia de Pino con variedad "Parana".
        """
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")

    @staticmethod
    def _crear_olivo() -> 'Cultivo':
        """Crea una instancia de Olivo con configuración por defecto.

        Retorna:
            Cultivo: Instancia de Olivo con tipo de aceituna ARBEQUINA.
        """
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> 'Cultivo':
        """Crea una instancia de Lechuga con configuración por defecto.

        Retorna:
            Cultivo: Instancia de Lechuga con variedad "Crespa".
        """
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Crespa")

    @staticmethod
    def _crear_zanahoria() -> 'Cultivo':
        """Crea una instancia de Zanahoria con configuración por defecto.

        Retorna:
            Cultivo: Instancia de Zanahoria tipo baby carrot.
        """
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(is_baby_carrot=True)


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 31/66: __init__.py
# Directorio: patrones/observer
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/observer/__init__.py
# ==============================================================================

from .observable import Observable
from .observer import Observer

__all__ = [
    'Observable',
    'Observer'
]

# ==============================================================================
# ARCHIVO 32/66: observable.py
# Directorio: patrones/observer
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/observer/observable.py
# ==============================================================================

from typing import Generic, TypeVar, List
from .observer import Observer

T = TypeVar('T')


class Observable(Generic[T]):
    """Clase base para implementar el patrón Observer (Observable).

    Esta clase permite que los objetos notifiquen automáticamente a sus
    observadores cuando ocurren cambios de estado. Usa genéricos para
    proporcionar type-safety en las notificaciones.

    Atributos:
        _observadores (List[Observer[T]]): Lista de observadores registrados.

    Type Parameters:
        T: Tipo de evento que se notifica a los observadores.
    """

    def __init__(self):
        """Inicializa un nuevo Observable sin observadores."""
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Registra un observador para recibir notificaciones.

        Argumentos:
            observador (Observer[T]): Observador a agregar. Si ya está registrado,
                no se agrega nuevamente.
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador de la lista de notificaciones.

        Argumentos:
            observador (Observer[T]): Observador a eliminar. Si no está registrado,
                no hace nada.
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores registrados sobre un evento.

        Argumentos:
            evento (T): Evento a notificar a los observadores.
        """
        for observador in self._observadores:
            observador.actualizar(evento)

# ==============================================================================
# ARCHIVO 33/66: observer.py
# Directorio: patrones/observer
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/observer/observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """Interfaz abstracta para implementar el patrón Observer.

    Define el contrato que deben cumplir todos los observadores para
    recibir notificaciones de objetos Observable. Usa genéricos para
    proporcionar type-safety.

    Type Parameters:
        T: Tipo de evento que el observador puede procesar.
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Procesa una notificación del objeto observable.

        Argumentos:
            evento (T): Evento recibido del observable que contiene
                información sobre el cambio de estado.
        """
        pass


################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 34/66: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 35/66: evento_plantacion.py
# Directorio: patrones/observer/eventos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/66: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 37/66: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 38/66: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================

from .absorcion_agua_strategy import AbsorcionAguaStrategy
from .impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from .impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

__all__ = [
    'AbsorcionAguaStrategy',
    'AbsorcionSeasonalStrategy',
    'AbsorcionConstanteStrategy'
]

# ==============================================================================
# ARCHIVO 39/66: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """Estrategia abstracta para calcular la absorción de agua de cultivos.

    Implementa el patrón Strategy para permitir diferentes algoritmos de
    cálculo de absorción de agua. Esto permite cambiar el comportamiento
    del cálculo en tiempo de ejecución sin modificar los servicios que lo usan.

    Las implementaciones concretas pueden considerar factores como estacionalidad,
    temperatura, humedad, y características específicas del cultivo.
    """

    @abstractmethod
    def calcular_absorcion(self, fecha: date, temperatura: float,
                           humedad: float, cultivo: 'Cultivo') -> int:
        """Calcula la cantidad de agua absorbida por un cultivo.

        Argumentos:
            fecha (date): Fecha del cálculo para considerar estacionalidad.
            temperatura (float): Temperatura ambiental en grados Celsius.
            humedad (float): Porcentaje de humedad ambiental (0-100).
            cultivo (Cultivo): Instancia del cultivo para el cual calcular absorción.

        Retorna:
            int: Cantidad de agua absorbida en litros.
        """
        pass


################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 40/66: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 41/66: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción de agua con valor constante.

    Calcula la absorción de agua devolviendo siempre una cantidad fija,
    sin considerar factores externos como temperatura, humedad o estación.

    Esta estrategia es útil para simplificar cálculos o para cultivos que
    tienen un consumo de agua predecible y constante.

    Atributos:
        _cantidad (int): Cantidad constante de agua a absorber en litros.
    """

    def __init__(self, cantidad_constante: int):
        """Inicializa la estrategia con una cantidad constante.

        Argumentos:
            cantidad_constante (int): Cantidad fija de agua a absorber en litros.
        """
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha: date, temperatura: float,
                           humedad: float, cultivo: 'Cultivo') -> int:
        """Calcula la absorción de agua devolviendo siempre el valor constante.

        Argumentos:
            fecha (date): No usado en esta estrategia.
            temperatura (float): No usado en esta estrategia.
            humedad (float): No usado en esta estrategia.
            cultivo (Cultivo): No usado en esta estrategia.

        Retorna:
            int: Cantidad constante de agua absorbida en litros.
        """
        return self._cantidad

# ==============================================================================
# ARCHIVO 42/66: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción de agua basada en estacionalidad.

    Calcula la absorción de agua considerando la estación del año.
    En verano, los cultivos absorben más agua que en invierno.

    Esta estrategia es útil para simular comportamientos realistas de
    cultivos que tienen diferentes necesidades hídricas según la época del año.
    """

    def calcular_absorcion(self, fecha: date, temperatura: float,
                           humedad: float, cultivo: 'Cultivo') -> int:
        """Calcula la absorción de agua según la estación del año.

        Argumentos:
            fecha (date): Fecha del cálculo para determinar la estación.
            temperatura (float): No usado en esta estrategia.
            humedad (float): No usado en esta estrategia.
            cultivo (Cultivo): No usado en esta estrategia.

        Retorna:
            int: Cantidad de agua absorbida en litros. Valor alto en verano,
                valor bajo en invierno.
        """
        mes = fecha.month

        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO


################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 43/66: __init__.py
# Directorio: riego
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 44/66: __init__.py
# Directorio: riego/control
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/control/__init__.py
# ==============================================================================

from .control_riego_task import ControlRiegoTask

__all__ = [
    'ControlRiegoTask'
]

# ==============================================================================
# ARCHIVO 45/66: control_riego_task.py
# Directorio: riego/control
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

import threading
import time
from typing import TYPE_CHECKING
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)

if TYPE_CHECKING:
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService


class ControlRiegoTask(threading.Thread, Observer[float]):
    """Controlador automático de riego que ejecuta en un hilo separado.

    Implementa el patrón Observer para recibir actualizaciones de los sensores
    de temperatura y humedad. Activa el riego automáticamente cuando las
    condiciones son adecuadas.

    El riego se activa si:
    - La temperatura está en el rango [TEMP_MIN_RIEGO, TEMP_MAX_RIEGO]
    - La humedad es menor a HUMEDAD_MAX_RIEGO

    Atributos:
        _sensor_temperatura (TemperaturaReaderTask): Sensor de temperatura observado.
        _sensor_humedad (HumedadReaderTask): Sensor de humedad observado.
        _plantacion (Plantacion): Plantación a regar.
        _plantacion_service (PlantacionService): Servicio para ejecutar el riego.
        _detenido (threading.Event): Event para detener el thread de forma segura.
        _ultima_temperatura (float): Última temperatura leída.
        _ultima_humedad (float): Última humedad leída.
    """

    def __init__(self, sensor_temperatura: 'TemperaturaReaderTask',
                 sensor_humedad: 'HumedadReaderTask',
                 plantacion: 'Plantacion',
                 plantacion_service: 'PlantacionService'):
        """Inicializa el controlador de riego.

        Se registra como observador de ambos sensores.

        Argumentos:
            sensor_temperatura (TemperaturaReaderTask): Sensor de temperatura.
            sensor_humedad (HumedadReaderTask): Sensor de humedad.
            plantacion (Plantacion): Plantación a controlar.
            plantacion_service (PlantacionService): Servicio para operaciones de riego.
        """
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()
        self._ultima_temperatura = 0.0
        self._ultima_humedad = 0.0

        self._sensor_temperatura.agregar_observador(self)
        self._sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """Recibe notificaciones de los sensores (método del patrón Observer).

        Argumentos:
            evento (float): Valor leído por el sensor (temperatura o humedad).
        """
        pass

    def run(self) -> None:
        """Ejecuta el ciclo principal del controlador de riego.

        Evalúa periódicamente las condiciones de temperatura y humedad.
        Activa el riego si se cumplen las condiciones. Se detiene automáticamente
        si se agota el agua.
        """
        while not self._detenido.is_set():
            try:
                if (TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO and
                        self._ultima_humedad < HUMEDAD_MAX_RIEGO):
                    self._plantacion_service.regar(self._plantacion)

                time.sleep(INTERVALO_CONTROL_RIEGO)
            except AguaAgotadaException as e:
                print(f"\n{e.get_full_message()}")
                print("Sistema de riego detenido automaticamente por falta de agua.")
                break

    def detener(self) -> None:
        """Detiene el thread del controlador de forma segura.

        Establece el flag de detenido para que el ciclo run() termine.
        """
        self._detenido.set()


################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 46/66: __init__.py
# Directorio: riego/sensores
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/sensores/__init__.py
# ==============================================================================

from .temperatura_reader_task import TemperaturaReaderTask
from .humedad_reader_task import HumedadReaderTask

__all__ = [
    'TemperaturaReaderTask',
    'HumedadReaderTask'
]

# ==============================================================================
# ARCHIVO 47/66: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX
)


class HumedadReaderTask(threading.Thread, Observable[float]):
    """Tarea que simula un sensor de humedad en un hilo separado.

    Implementa el patrón Observer como Observable, notificando a los observadores
    cada vez que lee un nuevo valor de humedad. Ejecuta en un thread daemon.

    La humedad se genera aleatoriamente dentro de un rango configurable.

    Atributos:
        _detenido (threading.Event): Event para detener el thread de forma segura.
    """

    def __init__(self):
        """Inicializa el sensor de humedad como thread daemon y observable."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Ejecuta el ciclo principal del sensor.

        Lee la humedad periódicamente, la imprime y notifica a los observadores.
        Continúa hasta que se invoque detener().
        """
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            print(f"[Humedad] {humedad:.2f} %")
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)

    def _leer_humedad(self) -> float:
        """Simula la lectura de humedad del sensor.

        Retorna:
            float: Humedad aleatoria en porcentaje (0-100) dentro del rango configurado.
        """
        return SENSOR_HUMEDAD_MIN + random.random() * (SENSOR_HUMEDAD_MAX - SENSOR_HUMEDAD_MIN)

    def detener(self) -> None:
        """Detiene el thread del sensor de forma segura.

        Establece el flag de detenido para que el ciclo run() termine.
        """
        self._detenido.set()

# ==============================================================================
# ARCHIVO 48/66: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)


class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """Tarea que simula un sensor de temperatura en un hilo separado.

    Implementa el patrón Observer como Observable, notificando a los observadores
    cada vez que lee una nueva temperatura. Ejecuta en un thread daemon.

    La temperatura se genera aleatoriamente dentro de un rango configurable.

    Atributos:
        _detenido (threading.Event): Event para detener el thread de forma segura.
    """

    def __init__(self):
        """Inicializa el sensor de temperatura como thread daemon y observable."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Ejecuta el ciclo principal del sensor.

        Lee la temperatura periódicamente, la imprime y notifica a los observadores.
        Continúa hasta que se invoque detener().
        """
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            print(f"[Temperatura] {temperatura:.2f} °C")
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def _leer_temperatura(self) -> float:
        """Simula la lectura de temperatura del sensor.

        Retorna:
            float: Temperatura aleatoria en grados Celsius dentro del rango configurado.
        """
        return SENSOR_TEMP_MIN + random.random() * (SENSOR_TEMP_MAX - SENSOR_TEMP_MIN)

    def detener(self) -> None:
        """Detiene el thread del sensor de forma segura.

        Establece el flag de detenido para que el ciclo run() termine.
        """
        self._detenido.set()


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 49/66: __init__.py
# Directorio: servicios
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 50/66: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================

from .cultivo_service import CultivoService
from .arbol_service import ArbolService
from .pino_service import PinoService
from .olivo_service import OlivoService
from .lechuga_service import LechugaService
from .zanahoria_service import ZanahoriaService
from .cultivo_service_registry import CultivoServiceRegistry

__all__ = [
    'CultivoService',
    'ArbolService',
    'PinoService',
    'OlivoService',
    'LechugaService',
    'ZanahoriaService',
    'CultivoServiceRegistry'
]

# ==============================================================================
# ARCHIVO 51/66: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

from typing import TYPE_CHECKING
from .cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """Servicio para operaciones específicas con árboles.

    Extiende CultivoService agregando funcionalidad específica para árboles
    como el crecimiento en altura.
    """

    def crecer(self, arbol: 'Arbol', incremento: float) -> None:
        """Aumenta la altura del árbol.

        Argumentos:
            arbol (Arbol): Árbol que crecerá.
            incremento (float): Incremento de altura en metros. Debe ser positivo.
        """
        if incremento > 0:
            arbol.set_altura(arbol.get_altura() + incremento)

# ==============================================================================
# ARCHIVO 52/66: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

from abc import ABC
from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService(ABC):
    """Servicio base abstracto para operaciones con cultivos.

    Implementa el patrón Strategy para delegar el cálculo de absorción de agua
    a diferentes estrategias. Proporciona funcionalidad común a todos los
    servicios de cultivo.

    Atributos:
        _estrategia_absorcion (AbsorcionAguaStrategy): Estrategia de cálculo de absorción.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """Inicializa el servicio con una estrategia de absorción.

        Argumentos:
            estrategia_absorcion (AbsorcionAguaStrategy): Estrategia para calcular
                la absorción de agua del cultivo.
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """Calcula y aplica la absorción de agua al cultivo.

        Delega el cálculo de absorción a la estrategia configurada y actualiza
        la cantidad de agua del cultivo.

        Argumentos:
            cultivo (Cultivo): Cultivo que absorberá agua.

        Retorna:
            int: Cantidad de agua absorbida en litros.
        """
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha=date.today(),
            temperatura=20.0,
            humedad=50.0,
            cultivo=cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Muestra información básica del cultivo por consola.

        Argumentos:
            cultivo (Cultivo): Cultivo del cual mostrar información.
        """
        print(f"Cultivo: {cultivo.__class__.__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")

# ==============================================================================
# ARCHIVO 53/66: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

from threading import Lock
from typing import TYPE_CHECKING, Dict, Type

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoServiceRegistry:
    """Registro centralizado de servicios para diferentes tipos de cultivos.

    Implementa el patrón Singleton para garantizar una única instancia del registro.
    Usa thread-safe double-checked locking para la inicialización.

    Este registro actúa como un dispatcher que delega las operaciones a los
    servicios específicos según el tipo de cultivo, evitando el uso de
    condicionales if/elif en el código cliente.

    Atributos:
        _instance (CultivoServiceRegistry): Instancia única del singleton.
        _lock (Lock): Lock para garantizar thread-safety en la creación.
        _initialized (bool): Indica si la instancia ya fue inicializada.
        _pino_service (PinoService): Servicio para pinos.
        _olivo_service (OlivoService): Servicio para olivos.
        _lechuga_service (LechugaService): Servicio para lechugas.
        _zanahoria_service (ZanahoriaService): Servicio para zanahorias.
        _absorber_agua_handlers (Dict): Mapeo de tipos a métodos de absorción.
        _mostrar_datos_handlers (Dict): Mapeo de tipos a métodos de visualización.
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        """Crea o retorna la instancia única del singleton.

        Usa double-checked locking para garantizar thread-safety sin
        afectar el rendimiento después de la primera creación.

        Retorna:
            CultivoServiceRegistry: Instancia única del registro.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Inicializa el registro con todos los servicios y handlers.

        Solo se ejecuta una vez gracias al flag _initialized.
        Registra los servicios y configura los mapeos de tipos a métodos.
        """
        if self._initialized:
            return

        from .pino_service import PinoService
        from .olivo_service import OlivoService
        from .lechuga_service import LechugaService
        from .zanahoria_service import ZanahoriaService
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        self._absorber_agua_handlers: Dict[Type, any] = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        self._mostrar_datos_handlers: Dict[Type, any] = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

        self._initialized = True

    @classmethod
    def get_instance(cls):
        """Obtiene la instancia única del registro.

        Retorna:
            CultivoServiceRegistry: Instancia única del singleton.
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """Delega la operación de absorción de agua al servicio apropiado.

        Argumentos:
            cultivo (Cultivo): Cultivo que absorberá agua.

        Retorna:
            int: Cantidad de agua absorbida en litros.

        Raises:
            ValueError: Si el tipo de cultivo no está registrado.
        """
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo)

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Delega la operación de mostrar datos al servicio apropiado.

        Argumentos:
            cultivo (Cultivo): Cultivo del cual mostrar información.

        Raises:
            ValueError: Si el tipo de cultivo no está registrado.
        """
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._mostrar_datos_handlers[tipo](cultivo)

    def _absorber_agua_pino(self, cultivo):
        """Handler privado para absorción de agua en pinos."""
        return self._pino_service.absorver_agua(cultivo)

    def _absorber_agua_olivo(self, cultivo):
        """Handler privado para absorción de agua en olivos."""
        return self._olivo_service.absorver_agua(cultivo)

    def _absorber_agua_lechuga(self, cultivo):
        """Handler privado para absorción de agua en lechugas."""
        return self._lechuga_service.absorver_agua(cultivo)

    def _absorber_agua_zanahoria(self, cultivo):
        """Handler privado para absorción de agua en zanahorias."""
        return self._zanahoria_service.absorver_agua(cultivo)

    def _mostrar_datos_pino(self, cultivo):
        """Handler privado para mostrar datos de pinos."""
        self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo):
        """Handler privado para mostrar datos de olivos."""
        self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo):
        """Handler privado para mostrar datos de lechugas."""
        self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo):
        """Handler privado para mostrar datos de zanahorias."""
        self._zanahoria_service.mostrar_datos(cultivo)

# ==============================================================================
# ARCHIVO 54/66: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

from typing import TYPE_CHECKING
from .cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """Servicio específico para operaciones con lechugas.

    Extiende CultivoService usando estrategia de absorción constante.
    Las lechugas absorben siempre la misma cantidad de agua.
    """

    def __init__(self):
        """Inicializa el servicio con estrategia de absorción constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))

    def mostrar_datos(self, lechuga: 'Lechuga') -> None:
        """Muestra información detallada de la lechuga por consola.

        Argumentos:
            lechuga (Lechuga): Lechuga de la cual mostrar información.
        """
        print(f"Cultivo: Lechuga")
        print(f"Superficie: {lechuga.get_superficie()} m²")
        print(f"Agua almacenada: {lechuga.get_agua()} L")
        print(f"Variedad: {lechuga.get_variedad()}")
        invernadero = "Si" if lechuga.get_invernadero() else "No"
        print(f"Invernadero: {invernadero}")

# ==============================================================================
# ARCHIVO 55/66: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

from typing import TYPE_CHECKING
from .arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """Servicio específico para operaciones con olivos.

    Extiende ArbolService usando estrategia de absorción estacional.
    Los olivos crecen automáticamente cada vez que absorben agua.
    """

    def __init__(self):
        """Inicializa el servicio con estrategia de absorción estacional."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, olivo: 'Olivo') -> int:
        """Absorbe agua y hace crecer el olivo automáticamente.

        Argumentos:
            olivo (Olivo): Olivo que absorberá agua.

        Retorna:
            int: Cantidad de agua absorbida en litros.
        """
        agua_absorvida = super().absorver_agua(olivo)
        self.crecer(olivo, CRECIMIENTO_OLIVO_POR_RIEGO)
        return agua_absorvida

    def mostrar_datos(self, olivo: 'Olivo') -> None:
        """Muestra información detallada del olivo por consola.

        Argumentos:
            olivo (Olivo): Olivo del cual mostrar información.
        """
        print(f"Cultivo: Olivo")
        print(f"Superficie: {olivo.get_superficie()} m²")
        print(f"Agua almacenada: {olivo.get_agua()} L")
        print(f"ID: {olivo.get_id()}")
        print(f"Altura: {olivo.get_altura()} m")
        print(f"Tipo de aceituna: {olivo.get_tipo().name}")

# ==============================================================================
# ARCHIVO 56/66: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

### ARCHIVO: python_forestacion/servicios/cultivos/pino_service.py

from typing import TYPE_CHECKING
from .arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """Servicio específico para operaciones con pinos.

    Extiende ArbolService usando estrategia de absorción estacional.
    Los pinos crecen automáticamente cada vez que absorben agua.
    """

    def __init__(self):
        """Inicializa el servicio con estrategia de absorción estacional."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, pino: 'Pino') -> int:
        """Absorbe agua y hace crecer el pino automáticamente.

        Argumentos:
            pino (Pino): Pino que absorberá agua.

        Retorna:
            int: Cantidad de agua absorbida en litros.
        """
        agua_absorvida = super().absorver_agua(pino)
        self.crecer(pino, CRECIMIENTO_PINO_POR_RIEGO)
        return agua_absorvida

    def mostrar_datos(self, pino: 'Pino') -> None:
        """Muestra información detallada del pino por consola.

        Argumentos:
            pino (Pino): Pino del cual mostrar información.
        """
        print(f"Cultivo: Pino")
        print(f"Superficie: {pino.get_superficie()} m²")
        print(f"Agua almacenada: {pino.get_agua()} L")
        print(f"ID: {pino.get_id()}")
        print(f"Altura: {pino.get_altura()} m")
        print(f"Variedad: {pino.get_variedad()}")

# ==============================================================================
# ARCHIVO 57/66: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

from typing import TYPE_CHECKING
from .cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """Servicio específico para operaciones con zanahorias.

    Extiende CultivoService usando estrategia de absorción constante.
    Las zanahorias absorben siempre la misma cantidad de agua.
    """

    def __init__(self):
        """Inicializa el servicio con estrategia de absorción constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_ZANAHORIA))

    def mostrar_datos(self, zanahoria: 'Zanahoria') -> None:
        """Muestra información detallada de la zanahoria por consola.

        Argumentos:
            zanahoria (Zanahoria): Zanahoria de la cual mostrar información.
        """
        print(f"Cultivo: Zanahoria")
        print(f"Superficie: {zanahoria.get_superficie()} m²")
        print(f"Agua almacenada: {zanahoria.get_agua()} L")
        baby = "Si" if zanahoria.is_baby_carrot() else "No"
        print(f"Es baby carrot: {baby}")


################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 58/66: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================

from .fincas_service import FincasService
from .paquete import Paquete

__all__ = [
    'FincasService',
    'Paquete'
]

# ==============================================================================
# ARCHIVO 59/66: fincas_service.py
# Directorio: servicios/negocio
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================

from typing import TYPE_CHECKING, Dict, Type, TypeVar
from .paquete import Paquete

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
    from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar('T')


class FincasService:
    """Servicio de gestión de operaciones de negocio para múltiples fincas.

    Centraliza la gestión de múltiples fincas (registros forestales), permitiendo
    operaciones como fumigación, cosecha y empaquetado de cultivos. Mantiene
    un registro de todas las fincas en el sistema.

    Attributos:
        _plantacion_service (PlantacionService): Servicio para operaciones en plantaciones.
        _cultivo_service_registry (CultivoServiceRegistry): Registro de servicios de cultivos.
        _fincas (Dict[int, RegistroForestal]): Diccionario de fincas indexadas por ID de padrón.
    """

    def __init__(self, plantacion_service: 'PlantacionService',
                 cultivo_service_registry: 'CultivoServiceRegistry'):
        """Inicializa el servicio de fincas.

        Argumentos:
            plantacion_service (PlantacionService): Servicio para gestionar plantaciones.
            cultivo_service_registry (CultivoServiceRegistry): Registro para operaciones
                con cultivos.
        """
        self._plantacion_service = plantacion_service
        self._cultivo_service_registry = cultivo_service_registry
        self._fincas: Dict[int, 'RegistroForestal'] = {}

    def add_finca(self, finca: 'RegistroForestal') -> None:
        """Agrega una finca al registro del servicio.

        La finca se indexa por su ID de padrón catastral.

        Argumentos:
            finca (RegistroForestal): Finca a agregar al registro.
        """
        self._fincas[finca.get_id_padron()] = finca

    def buscar_finca(self, id_padron: int) -> 'RegistroForestal':
        """Busca una finca por su ID de padrón catastral.

        Argumentos:
            id_padron (int): ID del padrón catastral de la finca.

        Retorna:
            RegistroForestal: Finca encontrada o None si no existe.
        """
        return self._fincas.get(id_padron)

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """Fumiga una plantación específica con un plaguicida.

        Busca la finca por su ID de padrón y aplica el plaguicida especificado.
        Si la finca no existe, no realiza ninguna acción.

        Argumentos:
            id_padron (int): ID del padrón de la finca a fumigar.
            plaguicida (str): Nombre o tipo de plaguicida a aplicar.
        """
        finca = self.buscar_finca(id_padron)
        if finca:
            print(f"\nFumigando plantacion con: {plaguicida}")

    def cosechar_yempaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
        """Cosecha y empaqueta todos los cultivos de un tipo específico de todas las fincas.

        Recorre todas las fincas registradas, identifica los cultivos del tipo especificado,
        los cosecha (elimina de la plantación) y los empaqueta en una caja genérica.

        Argumentos:
            tipo_cultivo (Type[T]): Clase del tipo de cultivo a cosechar
                (ej: Lechuga, Pino, Olivo).

        Retorna:
            Paquete[T]: Paquete genérico conteniendo todos los cultivos cosechados
                del tipo especificado.

        Tipo de parámetros:
            T: Tipo de cultivo que se cosechará y empaquetará.
        """
        caja = Paquete[T]()

        for finca in self._fincas.values():
            plantacion = finca.get_plantacion()
            cultivos_cosechados = []

            for cultivo in plantacion.get_cultivos():
                if isinstance(cultivo, tipo_cultivo):
                    cultivos_cosechados.append(cultivo)
                    caja.agregar_item(cultivo)

            if cultivos_cosechados:
                print(f"\nCOSECHANDO {len(cultivos_cosechados)} unidades de {tipo_cultivo.__name__}")
                self._plantacion_service.consumir(plantacion, tipo_cultivo)

        return caja

# ==============================================================================
# ARCHIVO 60/66: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================

from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """Contenedor genérico para empaquetar ítems del mismo tipo.

    Implementa un paquete o caja genérica que puede contener múltiples ítems
    de un tipo específico. Utiliza TypeVar para proporcionar type-safety en
    tiempo de desarrollo. Cada paquete tiene un ID único generado mediante
    un contador de clase.

    Atributos:
        _contador_id (int): Contador de clase para generar IDs únicos.
        _id (int): Identificador único del paquete.
        _items (List[T]): Lista de ítems contenidos en el paquete.

    Tipo de parámetros:
        T: Tipo de ítems que contendrá el paquete (ej: Lechuga, Pino, Olivo).

    Ejemplos:
        >>> paquete_lechugas = Paquete[Lechuga]()
        >>> paquete_lechugas.agregar_item(lechuga1)
        >>> paquete_lechugas.mostrar_contenido_caja()
    """

    _contador_id = 0

    def __init__(self):
        """Inicializa un nuevo paquete vacío con ID único.

        El ID se genera automáticamente incrementando el contador de clase,
        garantizando que cada paquete tenga un identificador único en el sistema.
        """
        Paquete._contador_id += 1
        self._id = Paquete._contador_id
        self._items: List[T] = []

    def agregar_item(self, item: T) -> None:
        """Agrega un ítem al paquete.

        Argumentos:
            item (T): Ítem a agregar al paquete. Debe ser del tipo especificado
                en el genérico del paquete.
        """
        self._items.append(item)

    def get_items(self) -> List[T]:
        """Obtiene una copia de la lista de ítems del paquete.

        Retorna una copia para evitar modificaciones externas de la lista interna.

        Retorna:
            List[T]: Copia de la lista de ítems contenidos en el paquete.
        """
        return self._items.copy()

    def mostrar_contenido_caja(self) -> None:
        """Muestra por consola el contenido del paquete.

        Imprime información resumida del paquete incluyendo el tipo de ítems,
        la cantidad y el ID del paquete. Si el paquete está vacío, lo indica.
        """
        print("\nContenido de la caja:")
        if self._items:
            print(f"  Tipo: {self._items[0].__class__.__name__}")
            print(f"  Cantidad: {len(self._items)}")
            print(f"  ID Paquete: {self._id}")
        else:
            print("  (vacia)")


################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 61/66: __init__.py
# Directorio: servicios/personal
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/personal/__init__.py
# ==============================================================================

from .trabajador_service import TrabajadorService

__all__ = [
    'TrabajadorService'
]

# ==============================================================================
# ARCHIVO 62/66: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.entidades.personal.apto_medico import AptoMedico

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.herramienta import Herramienta
    from python_forestacion.entidades.personal.tarea import Tarea


class TrabajadorService:
    """Servicio para gestionar operaciones relacionadas con trabajadores.

    Proporciona funcionalidad para asignar certificados médicos a trabajadores
    y ejecutar tareas asignadas verificando las condiciones necesarias como
    aptitud médica y disponibilidad de herramientas.
    """

    def asignar_apto_medico(self, trabajador: 'Trabajador', apto: bool,
                            fecha_emision: date, observaciones: str) -> None:
        """Asigna o actualiza el certificado de apto médico de un trabajador.

        Crea un nuevo certificado de aptitud médica y lo asigna al trabajador,
        reemplazando cualquier certificado anterior.

        Argumentos:
            trabajador (Trabajador): Trabajador al que se le asignará el certificado.
            apto (bool): True si el trabajador está apto para trabajar, False en caso contrario.
            fecha_emision (date): Fecha de emisión del certificado médico.
            observaciones (str): Observaciones o notas médicas adicionales.
        """
        apto_medico = AptoMedico(apto, fecha_emision, observaciones)
        trabajador.set_apto_medico(apto_medico)
        print(f"Apto medico actualizado para: {trabajador.get_nombre()}")

    def trabajar(self, trabajador: 'Trabajador', fecha: date, util: 'Herramienta') -> bool:
        """Ejecuta las tareas del trabajador para una fecha específica.

        Verifica que el trabajador tenga apto médico válido y ejecuta todas las
        tareas asignadas para la fecha especificada. Las tareas se procesan en
        orden descendente por ID y se marcan como completadas al ejecutarse.

        Argumentos:
            trabajador (Trabajador): Trabajador que ejecutará las tareas.
            fecha (date): Fecha para la cual se ejecutarán las tareas.
            util (Herramienta): Herramienta que el trabajador utilizará para las tareas.

        Retorna:
            bool: True si se ejecutó al menos una tarea, False si no se ejecutó ninguna
                o si el trabajador no tiene apto médico válido.
        """
        if not trabajador.get_apto_medico().esta_apto():
            print(f"El trabajador {trabajador.get_nombre()} no puede trabajar - apto medico invalido")
            return False

        tareas_ordenadas = sorted(trabajador.get_tareas(),
                                  key=self._obtener_id_tarea,
                                  reverse=True)

        tarea_ejecutada = False
        for tarea in tareas_ordenadas:
            if tarea.get_fecha() == fecha:
                print(f"El trabajador {trabajador.get_nombre()} realizo la tarea "
                      f"{tarea.get_id()} {tarea.get_descripcion()} con herramienta: {util.get_nombre()}")
                tarea.set_estado(True)
                tarea_ejecutada = True

        return tarea_ejecutada

    @staticmethod
    def _obtener_id_tarea(tarea: 'Tarea') -> int:
        """Función auxiliar privada para obtener el ID de una tarea.

        Utilizada como función key en el ordenamiento de tareas.

        Argumentos:
            tarea (Tarea): Tarea de la cual obtener el ID.

        Retorna:
            int: ID de la tarea.
        """
        return tarea.get_id()


################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 63/66: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================

from .tierra_service import TierraService
from .plantacion_service import PlantacionService
from .registro_forestal_service import RegistroForestalService

__all__ = [
    'TierraService',
    'PlantacionService',
    'RegistroForestalService'
]

# ==============================================================================
# ARCHIVO 64/66: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

from typing import TYPE_CHECKING
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_MINIMA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry


class PlantacionService:
    """Servicio para gestionar operaciones sobre plantaciones.

    Proporciona funcionalidad para plantar cultivos, regar y consumir
    cultivos de una plantación. Valida restricciones de superficie y agua.

    Atributos:
        _cultivo_service_registry (CultivoServiceRegistry): Registro de servicios
            para operaciones específicas de cultivos.
    """

    def __init__(self, cultivo_service_registry: 'CultivoServiceRegistry'):
        """Inicializa el servicio de plantación.

        Argumentos:
            cultivo_service_registry (CultivoServiceRegistry): Registro para
                delegar operaciones específicas de cultivos.
        """
        self._cultivo_service_registry = cultivo_service_registry

    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """Planta una cantidad de cultivos de una especie en la plantación.

        Valida que haya suficiente superficie disponible antes de plantar.
        Usa la fábrica de cultivos para crear las instancias.

        Argumentos:
            plantacion (Plantacion): Plantación donde plantar.
            especie (str): Especie del cultivo a plantar.
            cantidad (int): Cantidad de cultivos a plantar.

        Raises:
            SuperficieInsuficienteException: Si no hay suficiente superficie
                disponible para plantar todos los cultivos.
        """
        superficie_ocupada = sum(c.get_superficie() for c in plantacion.get_cultivos_interno())
        superficie_tierra = plantacion.get_tierra().get_superficie()
        superficie_disponible = superficie_tierra - superficie_ocupada

        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            superficie_requerida = cultivo.get_superficie()

            if superficie_disponible >= superficie_requerida:
                plantacion.get_cultivos_interno().append(cultivo)
                superficie_disponible -= superficie_requerida
                print(f"Se planto un/a: {cultivo.__class__.__name__}")
            else:
                raise SuperficieInsuficienteException(
                    cultivo.__class__.__name__,
                    superficie_requerida,
                    superficie_disponible
                )

    def regar(self, plantacion: 'Plantacion') -> None:
        """Riega todos los cultivos de la plantación.

        Cada cultivo absorbe agua según su estrategia de absorción.
        El agua se descuenta del agua disponible de la plantación.

        Argumentos:
            plantacion (Plantacion): Plantación a regar.

        Raises:
            AguaAgotadaException: Si el agua disponible es menor al mínimo requerido.
        """
        print(f"Regando finca: {plantacion.get_nombre()}")

        for cultivo in plantacion.get_cultivos_interno():
            agua_actual = plantacion.get_agua_disponible()

            if agua_actual > AGUA_MINIMA:
                agua_absorvida = self._cultivo_service_registry.absorber_agua(cultivo)
                plantacion.set_agua_disponible(agua_actual - agua_absorvida)
            else:
                raise AguaAgotadaException(agua_actual, AGUA_MINIMA)

    def consumir(self, plantacion: 'Plantacion', tipo_cultivo: type) -> None:
        """Elimina todos los cultivos de un tipo específico de la plantación.

        Útil para simular cosecha o consumo de cultivos.

        Argumentos:
            plantacion (Plantacion): Plantación de donde eliminar cultivos.
            tipo_cultivo (type): Tipo de cultivo a eliminar.
        """
        cultivos = plantacion.get_cultivos_interno()
        for i in range(len(cultivos) - 1, -1, -1):
            if isinstance(cultivos[i], tipo_cultivo):
                cultivos.pop(i)

# ==============================================================================
# ARCHIVO 65/66: registro_forestal_service.py
# Directorio: servicios/terrenos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

import pickle
import os
from typing import TYPE_CHECKING
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
    from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry


class RegistroForestalService:
    """Servicio para gestionar operaciones sobre registros forestales.

    Proporciona funcionalidad para mostrar información de registros forestales,
    persistir registros en disco usando serialización pickle y recuperar registros
    desde archivos. Los archivos se almacenan en el directorio configurado usando
    el nombre del propietario como identificador.

    Atributos:
        _cultivo_service_registry (CultivoServiceRegistry): Registro de servicios
            para delegar operaciones de visualización de cultivos.
    """

    def __init__(self, cultivo_service_registry: 'CultivoServiceRegistry'):
        """Inicializa el servicio de registros forestales.

        Argumentos:
            cultivo_service_registry (CultivoServiceRegistry): Registro para
                operaciones con cultivos.
        """
        self._cultivo_service_registry = cultivo_service_registry

    def mostrar_datos(self, registro: 'RegistroForestal') -> None:
        """Muestra por consola toda la información de un registro forestal.

        Imprime información detallada del registro incluyendo datos del padrón,
        propietario, avalúo, tierra y un listado completo de todos los cultivos
        plantados con sus características específicas.

        Argumentos:
            registro (RegistroForestal): Registro forestal a mostrar.
        """
        print("\nREGISTRO FORESTAL")
        print("=================")
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")
        print(f"Domicilio:   {registro.get_tierra().get_domicilio()}")
        print(f"Superficie:  {registro.get_tierra().get_superficie()}")
        print(f"Cantidad de cultivos plantados: {len(registro.get_plantacion().get_cultivos())}")
        print("Listado de Cultivos plantados")
        print("____________________________")

        for cultivo in registro.get_plantacion().get_cultivos():
            self._cultivo_service_registry.mostrar_datos(cultivo)
            print()

    def persistir(self, registro: 'RegistroForestal') -> None:
        """Persiste un registro forestal en disco usando serialización pickle.

        Crea el directorio de datos si no existe y guarda el registro en un archivo
        binario con el nombre del propietario. Si ya existe un archivo con ese nombre,
        se sobrescribe.

        Argumentos:
            registro (RegistroForestal): Registro forestal a persistir.

        Raises:
            PersistenciaException: Si ocurre algún error durante la escritura del archivo.
        """
        os.makedirs(DIRECTORIO_DATA, exist_ok=True)

        nombre_archivo = f"{DIRECTORIO_DATA}/{registro.get_propietario()}{EXTENSION_DATA}"

        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(f"Registro de {registro.get_propietario()} persistido exitosamente en {nombre_archivo}")
        except Exception as e:
            raise PersistenciaException(f"Error al persistir: {str(e)}", nombre_archivo)

    @staticmethod
    def leer_registro(propietario: str) -> 'RegistroForestal':
        """Lee y deserializa un registro forestal desde disco.

        Busca un archivo con el nombre del propietario en el directorio de datos
        y deserializa el objeto RegistroForestal usando pickle.

        Argumentos:
            propietario (str): Nombre del propietario del registro a leer.
                No puede ser nulo ni vacío.

        Retorna:
            RegistroForestal: Registro forestal recuperado desde el archivo.

        Raises:
            ValueError: Si el nombre del propietario es nulo o vacío.
            PersistenciaException: Si el archivo no existe o si ocurre algún error
                durante la lectura o deserialización.
        """
        if not propietario or not propietario.strip():
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")

        nombre_archivo = f"{DIRECTORIO_DATA}/{propietario}{EXTENSION_DATA}"

        try:
            with open(nombre_archivo, 'rb') as f:
                registro = pickle.load(f)
            print(f"Registro de {propietario} recuperado exitosamente desde {nombre_archivo}")
            return registro
        except FileNotFoundError:
            raise PersistenciaException(f"Archivo no encontrado: {nombre_archivo}", nombre_archivo)
        except Exception as e:
            raise PersistenciaException(f"Error al leer: {str(e)}", nombre_archivo)

# ==============================================================================
# ARCHIVO 66/66: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION


class TierraService:
    """Servicio para gestionar operaciones sobre tierras.

    Proporciona funcionalidad para crear tierras con sus plantaciones asociadas,
    estableciendo correctamente la relación bidireccional entre ambas entidades.
    """

    def crear_tierra_con_plantacion(self, id_padron_catastral: int, superficie: float,
                                    domicilio: str, nombre_plantacion: str) -> Tierra:
        """Crea una tierra con una plantación asociada.

        Crea una instancia de Tierra y una de Plantación con la misma superficie,
        estableciendo la relación bidireccional entre ambas. La plantación se
        inicializa con la cantidad de agua configurada en las constantes.

        Argumentos:
            id_padron_catastral (int): Identificador único del padrón catastral.
            superficie (float): Superficie de la tierra en metros cuadrados.
                La plantación tendrá la misma superficie.
            domicilio (str): Dirección o ubicación de la tierra.
            nombre_plantacion (str): Nombre identificatorio de la plantación.

        Retorna:
            Tierra: Instancia de tierra creada con su plantación asociada.

        Raises:
            ValueError: Si la superficie es menor o igual a cero (validación en Tierra).
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        plantacion = Plantacion(nombre_plantacion, superficie, AGUA_INICIAL_PLANTACION)
        plantacion.set_tierra(tierra)
        tierra.set_finca(plantacion)

        print(f"Tierra creada: {domicilio} con plantacion: {nombre_plantacion}")
        return tierra


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 66
# Generado: 2025-10-21 21:15:59
################################################################################
