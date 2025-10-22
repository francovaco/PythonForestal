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