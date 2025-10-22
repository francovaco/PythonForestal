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