from typing import TYPE_CHECKING
from .arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """Servicio específico para operaciones con olivos.

    Extiende ArbolService usando estrategia de absorción estacional.
    Los olivos crecen automáticamente cada vez que absorben agua.
    """

    def __init__(self):
        """Inicializa el servicio con estrategia de absorción estacional."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, olivo: 'Olivo') -> int:
        """Absorbe agua y hace crecer el olivo automáticamente.

        Argumentos:
            olivo (Olivo): Olivo que absorberá agua.

        Retorna:
            int: Cantidad de agua absorbida en litros.
        """
        agua_absorvida = super().absorver_agua(olivo)
        self.crecer(olivo, CRECIMIENTO_OLIVO_POR_RIEGO)
        return agua_absorvida

    def mostrar_datos(self, olivo: 'Olivo') -> None:
        """Muestra información detallada del olivo por consola.

        Argumentos:
            olivo (Olivo): Olivo del cual mostrar información.
        """
        print(f"Cultivo: Olivo")
        print(f"Superficie: {olivo.get_superficie()} m²")
        print(f"Agua almacenada: {olivo.get_agua()} L")
        print(f"ID: {olivo.get_id()}")
        print(f"Altura: {olivo.get_altura()} m")
        print(f"Tipo de aceituna: {olivo.get_tipo().name}")