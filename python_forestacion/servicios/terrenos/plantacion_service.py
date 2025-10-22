from typing import TYPE_CHECKING
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_MINIMA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry


class PlantacionService:
    """Servicio para gestionar operaciones sobre plantaciones.

    Proporciona funcionalidad para plantar cultivos, regar y consumir
    cultivos de una plantación. Valida restricciones de superficie y agua.

    Atributos:
        _cultivo_service_registry (CultivoServiceRegistry): Registro de servicios
            para operaciones específicas de cultivos.
    """

    def __init__(self, cultivo_service_registry: 'CultivoServiceRegistry'):
        """Inicializa el servicio de plantación.

        Argumentos:
            cultivo_service_registry (CultivoServiceRegistry): Registro para
                delegar operaciones específicas de cultivos.
        """
        self._cultivo_service_registry = cultivo_service_registry

    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """Planta una cantidad de cultivos de una especie en la plantación.

        Valida que haya suficiente superficie disponible antes de plantar.
        Usa la fábrica de cultivos para crear las instancias.

        Argumentos:
            plantacion (Plantacion): Plantación donde plantar.
            especie (str): Especie del cultivo a plantar.
            cantidad (int): Cantidad de cultivos a plantar.

        Raises:
            SuperficieInsuficienteException: Si no hay suficiente superficie
                disponible para plantar todos los cultivos.
        """
        superficie_ocupada = sum(c.get_superficie() for c in plantacion.get_cultivos_interno())
        superficie_tierra = plantacion.get_tierra().get_superficie()
        superficie_disponible = superficie_tierra - superficie_ocupada

        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            superficie_requerida = cultivo.get_superficie()

            if superficie_disponible >= superficie_requerida:
                plantacion.get_cultivos_interno().append(cultivo)
                superficie_disponible -= superficie_requerida
                print(f"Se planto un/a: {cultivo.__class__.__name__}")
            else:
                raise SuperficieInsuficienteException(
                    cultivo.__class__.__name__,
                    superficie_requerida,
                    superficie_disponible
                )

    def regar(self, plantacion: 'Plantacion') -> None:
        """Riega todos los cultivos de la plantación.

        Cada cultivo absorbe agua según su estrategia de absorción.
        El agua se descuenta del agua disponible de la plantación.

        Argumentos:
            plantacion (Plantacion): Plantación a regar.

        Raises:
            AguaAgotadaException: Si el agua disponible es menor al mínimo requerido.
        """
        print(f"Regando finca: {plantacion.get_nombre()}")

        for cultivo in plantacion.get_cultivos_interno():
            agua_actual = plantacion.get_agua_disponible()

            if agua_actual > AGUA_MINIMA:
                agua_absorvida = self._cultivo_service_registry.absorber_agua(cultivo)
                plantacion.set_agua_disponible(agua_actual - agua_absorvida)
            else:
                raise AguaAgotadaException(agua_actual, AGUA_MINIMA)

    def consumir(self, plantacion: 'Plantacion', tipo_cultivo: type) -> None:
        """Elimina todos los cultivos de un tipo específico de la plantación.

        Útil para simular cosecha o consumo de cultivos.

        Argumentos:
            plantacion (Plantacion): Plantación de donde eliminar cultivos.
            tipo_cultivo (type): Tipo de cultivo a eliminar.
        """
        cultivos = plantacion.get_cultivos_interno()
        for i in range(len(cultivos) - 1, -1, -1):
            if isinstance(cultivos[i], tipo_cultivo):
                cultivos.pop(i)