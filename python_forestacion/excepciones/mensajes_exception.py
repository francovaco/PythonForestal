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