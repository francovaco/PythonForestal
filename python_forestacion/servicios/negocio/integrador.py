"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/negocio
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/negocio/__init__.py
# ================================================================================

from .fincas_service import FincasService
from .paquete import Paquete

__all__ = [
    'FincasService',
    'Paquete'
]

# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/negocio/fincas_service.py
# ================================================================================

from typing import TYPE_CHECKING, Dict, Type, TypeVar
from .paquete import Paquete

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
    from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar('T')


class FincasService:
    """Servicio de gestión de operaciones de negocio para múltiples fincas.

    Centraliza la gestión de múltiples fincas (registros forestales), permitiendo
    operaciones como fumigación, cosecha y empaquetado de cultivos. Mantiene
    un registro de todas las fincas en el sistema.

    Attributos:
        _plantacion_service (PlantacionService): Servicio para operaciones en plantaciones.
        _cultivo_service_registry (CultivoServiceRegistry): Registro de servicios de cultivos.
        _fincas (Dict[int, RegistroForestal]): Diccionario de fincas indexadas por ID de padrón.
    """

    def __init__(self, plantacion_service: 'PlantacionService',
                 cultivo_service_registry: 'CultivoServiceRegistry'):
        """Inicializa el servicio de fincas.

        Argumentos:
            plantacion_service (PlantacionService): Servicio para gestionar plantaciones.
            cultivo_service_registry (CultivoServiceRegistry): Registro para operaciones
                con cultivos.
        """
        self._plantacion_service = plantacion_service
        self._cultivo_service_registry = cultivo_service_registry
        self._fincas: Dict[int, 'RegistroForestal'] = {}

    def add_finca(self, finca: 'RegistroForestal') -> None:
        """Agrega una finca al registro del servicio.

        La finca se indexa por su ID de padrón catastral.

        Argumentos:
            finca (RegistroForestal): Finca a agregar al registro.
        """
        self._fincas[finca.get_id_padron()] = finca

    def buscar_finca(self, id_padron: int) -> 'RegistroForestal':
        """Busca una finca por su ID de padrón catastral.

        Argumentos:
            id_padron (int): ID del padrón catastral de la finca.

        Retorna:
            RegistroForestal: Finca encontrada o None si no existe.
        """
        return self._fincas.get(id_padron)

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """Fumiga una plantación específica con un plaguicida.

        Busca la finca por su ID de padrón y aplica el plaguicida especificado.
        Si la finca no existe, no realiza ninguna acción.

        Argumentos:
            id_padron (int): ID del padrón de la finca a fumigar.
            plaguicida (str): Nombre o tipo de plaguicida a aplicar.
        """
        finca = self.buscar_finca(id_padron)
        if finca:
            print(f"\nFumigando plantacion con: {plaguicida}")

    def cosechar_yempaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
        """Cosecha y empaqueta todos los cultivos de un tipo específico de todas las fincas.

        Recorre todas las fincas registradas, identifica los cultivos del tipo especificado,
        los cosecha (elimina de la plantación) y los empaqueta en una caja genérica.

        Argumentos:
            tipo_cultivo (Type[T]): Clase del tipo de cultivo a cosechar
                (ej: Lechuga, Pino, Olivo).

        Retorna:
            Paquete[T]: Paquete genérico conteniendo todos los cultivos cosechados
                del tipo especificado.

        Tipo de parámetros:
            T: Tipo de cultivo que se cosechará y empaquetará.
        """
        caja = Paquete[T]()

        for finca in self._fincas.values():
            plantacion = finca.get_plantacion()
            cultivos_cosechados = []

            for cultivo in plantacion.get_cultivos():
                if isinstance(cultivo, tipo_cultivo):
                    cultivos_cosechados.append(cultivo)
                    caja.agregar_item(cultivo)

            if cultivos_cosechados:
                print(f"\nCOSECHANDO {len(cultivos_cosechados)} unidades de {tipo_cultivo.__name__}")
                self._plantacion_service.consumir(plantacion, tipo_cultivo)

        return caja

# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/negocio/paquete.py
# ================================================================================

from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """Contenedor genérico para empaquetar ítems del mismo tipo.

    Implementa un paquete o caja genérica que puede contener múltiples ítems
    de un tipo específico. Utiliza TypeVar para proporcionar type-safety en
    tiempo de desarrollo. Cada paquete tiene un ID único generado mediante
    un contador de clase.

    Atributos:
        _contador_id (int): Contador de clase para generar IDs únicos.
        _id (int): Identificador único del paquete.
        _items (List[T]): Lista de ítems contenidos en el paquete.

    Tipo de parámetros:
        T: Tipo de ítems que contendrá el paquete (ej: Lechuga, Pino, Olivo).

    Ejemplos:
        >>> paquete_lechugas = Paquete[Lechuga]()
        >>> paquete_lechugas.agregar_item(lechuga1)
        >>> paquete_lechugas.mostrar_contenido_caja()
    """

    _contador_id = 0

    def __init__(self):
        """Inicializa un nuevo paquete vacío con ID único.

        El ID se genera automáticamente incrementando el contador de clase,
        garantizando que cada paquete tenga un identificador único en el sistema.
        """
        Paquete._contador_id += 1
        self._id = Paquete._contador_id
        self._items: List[T] = []

    def agregar_item(self, item: T) -> None:
        """Agrega un ítem al paquete.

        Argumentos:
            item (T): Ítem a agregar al paquete. Debe ser del tipo especificado
                en el genérico del paquete.
        """
        self._items.append(item)

    def get_items(self) -> List[T]:
        """Obtiene una copia de la lista de ítems del paquete.

        Retorna una copia para evitar modificaciones externas de la lista interna.

        Retorna:
            List[T]: Copia de la lista de ítems contenidos en el paquete.
        """
        return self._items.copy()

    def mostrar_contenido_caja(self) -> None:
        """Muestra por consola el contenido del paquete.

        Imprime información resumida del paquete incluyendo el tipo de ítems,
        la cantidad y el ID del paquete. Si el paquete está vacío, lo indica.
        """
        print("\nContenido de la caja:")
        if self._items:
            print(f"  Tipo: {self._items[0].__class__.__name__}")
            print(f"  Cantidad: {len(self._items)}")
            print(f"  ID Paquete: {self._id}")
        else:
            print("  (vacia)")

