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