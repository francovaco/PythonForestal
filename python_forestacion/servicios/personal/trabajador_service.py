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