### ARCHIVO: python_forestacion/servicios/cultivos/pino_service.py

from typing import TYPE_CHECKING
from .arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """Servicio específico para operaciones con pinos.

    Extiende ArbolService usando estrategia de absorción estacional.
    Los pinos crecen automáticamente cada vez que absorben agua.
    """

    def __init__(self):
        """Inicializa el servicio con estrategia de absorción estacional."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, pino: 'Pino') -> int:
        """Absorbe agua y hace crecer el pino automáticamente.

        Argumentos:
            pino (Pino): Pino que absorberá agua.

        Retorna:
            int: Cantidad de agua absorbida en litros.
        """
        agua_absorvida = super().absorver_agua(pino)
        self.crecer(pino, CRECIMIENTO_PINO_POR_RIEGO)
        return agua_absorvida

    def mostrar_datos(self, pino: 'Pino') -> None:
        """Muestra información detallada del pino por consola.

        Argumentos:
            pino (Pino): Pino del cual mostrar información.
        """
        print(f"Cultivo: Pino")
        print(f"Superficie: {pino.get_superficie()} m²")
        print(f"Agua almacenada: {pino.get_agua()} L")
        print(f"ID: {pino.get_id()}")
        print(f"Altura: {pino.get_altura()} m")
        print(f"Variedad: {pino.get_variedad()}")