from typing import TYPE_CHECKING
from .cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_CONSTANTE_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """Servicio específico para operaciones con zanahorias.

    Extiende CultivoService usando estrategia de absorción constante.
    Las zanahorias absorben siempre la misma cantidad de agua.
    """

    def __init__(self):
        """Inicializa el servicio con estrategia de absorción constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_CONSTANTE_ZANAHORIA))

    def mostrar_datos(self, zanahoria: 'Zanahoria') -> None:
        """Muestra información detallada de la zanahoria por consola.

        Argumentos:
            zanahoria (Zanahoria): Zanahoria de la cual mostrar información.
        """
        print(f"Cultivo: Zanahoria")
        print(f"Superficie: {zanahoria.get_superficie()} m²")
        print(f"Agua almacenada: {zanahoria.get_agua()} L")
        baby = "Si" if zanahoria.is_baby_carrot() else "No"
        print(f"Es baby carrot: {baby}")