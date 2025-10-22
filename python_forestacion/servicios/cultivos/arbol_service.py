from typing import TYPE_CHECKING
from .cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """Servicio para operaciones específicas con árboles.

    Extiende CultivoService agregando funcionalidad específica para árboles
    como el crecimiento en altura.
    """

    def crecer(self, arbol: 'Arbol', incremento: float) -> None:
        """Aumenta la altura del árbol.

        Argumentos:
            arbol (Arbol): Árbol que crecerá.
            incremento (float): Incremento de altura en metros. Debe ser positivo.
        """
        if incremento > 0:
            arbol.set_altura(arbol.get_altura() + incremento)