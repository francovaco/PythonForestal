"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal/__init__.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal/tarea.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

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

