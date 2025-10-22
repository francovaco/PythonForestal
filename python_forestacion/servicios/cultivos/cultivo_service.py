from abc import ABC
from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService(ABC):
    """Servicio base abstracto para operaciones con cultivos.

    Implementa el patrón Strategy para delegar el cálculo de absorción de agua
    a diferentes estrategias. Proporciona funcionalidad común a todos los
    servicios de cultivo.

    Atributos:
        _estrategia_absorcion (AbsorcionAguaStrategy): Estrategia de cálculo de absorción.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """Inicializa el servicio con una estrategia de absorción.

        Argumentos:
            estrategia_absorcion (AbsorcionAguaStrategy): Estrategia para calcular
                la absorción de agua del cultivo.
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """Calcula y aplica la absorción de agua al cultivo.

        Delega el cálculo de absorción a la estrategia configurada y actualiza
        la cantidad de agua del cultivo.

        Argumentos:
            cultivo (Cultivo): Cultivo que absorberá agua.

        Retorna:
            int: Cantidad de agua absorbida en litros.
        """
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha=date.today(),
            temperatura=20.0,
            humedad=50.0,
            cultivo=cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Muestra información básica del cultivo por consola.

        Argumentos:
            cultivo (Cultivo): Cultivo del cual mostrar información.
        """
        print(f"Cultivo: {cultivo.__class__.__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")