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