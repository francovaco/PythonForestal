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