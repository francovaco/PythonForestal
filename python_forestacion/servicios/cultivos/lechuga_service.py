from typing import TYPE_CHECKING
from .cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """Servicio específico para operaciones con lechugas.

    Extiende CultivoService usando estrategia de absorción constante.
    Las lechugas absorben siempre la misma cantidad de agua.
    """

    def __init__(self):
        """Inicializa el servicio con estrategia de absorción constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_LECHUGA))

    def mostrar_datos(self, lechuga: 'Lechuga') -> None:
        """Muestra información detallada de la lechuga por consola.

        Argumentos:
            lechuga (Lechuga): Lechuga de la cual mostrar información.
        """
        print(f"Cultivo: Lechuga")
        print(f"Superficie: {lechuga.get_superficie()} m²")
        print(f"Agua almacenada: {lechuga.get_agua()} L")
        print(f"Variedad: {lechuga.get_variedad()}")
        invernadero = "Si" if lechuga.get_invernadero() else "No"
        print(f"Invernadero: {invernadero}")