"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/__init__.py
# ================================================================================

from .absorcion_agua_strategy import AbsorcionAguaStrategy
from .impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from .impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

__all__ = [
    'AbsorcionAguaStrategy',
    'AbsorcionSeasonalStrategy',
    'AbsorcionConstanteStrategy'
]

# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """Estrategia abstracta para calcular la absorción de agua de cultivos.

    Implementa el patrón Strategy para permitir diferentes algoritmos de
    cálculo de absorción de agua. Esto permite cambiar el comportamiento
    del cálculo en tiempo de ejecución sin modificar los servicios que lo usan.

    Las implementaciones concretas pueden considerar factores como estacionalidad,
    temperatura, humedad, y características específicas del cultivo.
    """

    @abstractmethod
    def calcular_absorcion(self, fecha: date, temperatura: float,
                           humedad: float, cultivo: 'Cultivo') -> int:
        """Calcula la cantidad de agua absorbida por un cultivo.

        Argumentos:
            fecha (date): Fecha del cálculo para considerar estacionalidad.
            temperatura (float): Temperatura ambiental en grados Celsius.
            humedad (float): Porcentaje de humedad ambiental (0-100).
            cultivo (Cultivo): Instancia del cultivo para el cual calcular absorción.

        Retorna:
            int: Cantidad de agua absorbida en litros.
        """
        pass

