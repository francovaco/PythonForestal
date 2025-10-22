"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/__init__.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

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

