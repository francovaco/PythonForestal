from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción de agua basada en estacionalidad.

    Calcula la absorción de agua considerando la estación del año.
    En verano, los cultivos absorben más agua que en invierno.

    Esta estrategia es útil para simular comportamientos realistas de
    cultivos que tienen diferentes necesidades hídricas según la época del año.
    """

    def calcular_absorcion(self, fecha: date, temperatura: float,
                           humedad: float, cultivo: 'Cultivo') -> int:
        """Calcula la absorción de agua según la estación del año.

        Argumentos:
            fecha (date): Fecha del cálculo para determinar la estación.
            temperatura (float): No usado en esta estrategia.
            humedad (float): No usado en esta estrategia.
            cultivo (Cultivo): No usado en esta estrategia.

        Retorna:
            int: Cantidad de agua absorbida en litros. Valor alto en verano,
                valor bajo en invierno.
        """
        mes = fecha.month

        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO