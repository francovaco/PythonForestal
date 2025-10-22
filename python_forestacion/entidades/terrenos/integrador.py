"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/terrenos
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================

from .tierra import Tierra
from .plantacion import Plantacion
from .registro_forestal import RegistroForestal

__all__ = [
    'Tierra',
    'Plantacion',
    'RegistroForestal'
]

# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

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

