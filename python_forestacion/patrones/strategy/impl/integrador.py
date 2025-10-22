"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción de agua con valor constante.

    Calcula la absorción de agua devolviendo siempre una cantidad fija,
    sin considerar factores externos como temperatura, humedad o estación.

    Esta estrategia es útil para simplificar cálculos o para cultivos que
    tienen un consumo de agua predecible y constante.

    Atributos:
        _cantidad (int): Cantidad constante de agua a absorber en litros.
    """

    def __init__(self, cantidad_constante: int):
        """Inicializa la estrategia con una cantidad constante.

        Argumentos:
            cantidad_constante (int): Cantidad fija de agua a absorber en litros.
        """
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha: date, temperatura: float,
                           humedad: float, cultivo: 'Cultivo') -> int:
        """Calcula la absorción de agua devolviendo siempre el valor constante.

        Argumentos:
            fecha (date): No usado en esta estrategia.
            temperatura (float): No usado en esta estrategia.
            humedad (float): No usado en esta estrategia.
            cultivo (Cultivo): No usado en esta estrategia.

        Retorna:
            int: Cantidad constante de agua absorbida en litros.
        """
        return self._cantidad

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

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

