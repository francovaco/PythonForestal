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