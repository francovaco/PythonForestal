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