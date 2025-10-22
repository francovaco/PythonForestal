"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/terrenos
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================

from .tierra_service import TierraService
from .plantacion_service import PlantacionService
from .registro_forestal_service import RegistroForestalService

__all__ = [
    'TierraService',
    'PlantacionService',
    'RegistroForestalService'
]

# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

import pickle
import os
from typing import TYPE_CHECKING
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
    from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry


class RegistroForestalService:
    """Servicio para gestionar operaciones sobre registros forestales.

    Proporciona funcionalidad para mostrar información de registros forestales,
    persistir registros en disco usando serialización pickle y recuperar registros
    desde archivos. Los archivos se almacenan en el directorio configurado usando
    el nombre del propietario como identificador.

    Atributos:
        _cultivo_service_registry (CultivoServiceRegistry): Registro de servicios
            para delegar operaciones de visualización de cultivos.
    """

    def __init__(self, cultivo_service_registry: 'CultivoServiceRegistry'):
        """Inicializa el servicio de registros forestales.

        Argumentos:
            cultivo_service_registry (CultivoServiceRegistry): Registro para
                operaciones con cultivos.
        """
        self._cultivo_service_registry = cultivo_service_registry

    def mostrar_datos(self, registro: 'RegistroForestal') -> None:
        """Muestra por consola toda la información de un registro forestal.

        Imprime información detallada del registro incluyendo datos del padrón,
        propietario, avalúo, tierra y un listado completo de todos los cultivos
        plantados con sus características específicas.

        Argumentos:
            registro (RegistroForestal): Registro forestal a mostrar.
        """
        print("\nREGISTRO FORESTAL")
        print("=================")
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")
        print(f"Domicilio:   {registro.get_tierra().get_domicilio()}")
        print(f"Superficie:  {registro.get_tierra().get_superficie()}")
        print(f"Cantidad de cultivos plantados: {len(registro.get_plantacion().get_cultivos())}")
        print("Listado de Cultivos plantados")
        print("____________________________")

        for cultivo in registro.get_plantacion().get_cultivos():
            self._cultivo_service_registry.mostrar_datos(cultivo)
            print()

    def persistir(self, registro: 'RegistroForestal') -> None:
        """Persiste un registro forestal en disco usando serialización pickle.

        Crea el directorio de datos si no existe y guarda el registro en un archivo
        binario con el nombre del propietario. Si ya existe un archivo con ese nombre,
        se sobrescribe.

        Argumentos:
            registro (RegistroForestal): Registro forestal a persistir.

        Raises:
            PersistenciaException: Si ocurre algún error durante la escritura del archivo.
        """
        os.makedirs(DIRECTORIO_DATA, exist_ok=True)

        nombre_archivo = f"{DIRECTORIO_DATA}/{registro.get_propietario()}{EXTENSION_DATA}"

        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(f"Registro de {registro.get_propietario()} persistido exitosamente en {nombre_archivo}")
        except Exception as e:
            raise PersistenciaException(f"Error al persistir: {str(e)}", nombre_archivo)

    @staticmethod
    def leer_registro(propietario: str) -> 'RegistroForestal':
        """Lee y deserializa un registro forestal desde disco.

        Busca un archivo con el nombre del propietario en el directorio de datos
        y deserializa el objeto RegistroForestal usando pickle.

        Argumentos:
            propietario (str): Nombre del propietario del registro a leer.
                No puede ser nulo ni vacío.

        Retorna:
            RegistroForestal: Registro forestal recuperado desde el archivo.

        Raises:
            ValueError: Si el nombre del propietario es nulo o vacío.
            PersistenciaException: Si el archivo no existe o si ocurre algún error
                durante la lectura o deserialización.
        """
        if not propietario or not propietario.strip():
            raise ValueError("El nombre del propietario no puede ser nulo o vacio")

        nombre_archivo = f"{DIRECTORIO_DATA}/{propietario}{EXTENSION_DATA}"

        try:
            with open(nombre_archivo, 'rb') as f:
                registro = pickle.load(f)
            print(f"Registro de {propietario} recuperado exitosamente desde {nombre_archivo}")
            return registro
        except FileNotFoundError:
            raise PersistenciaException(f"Archivo no encontrado: {nombre_archivo}", nombre_archivo)
        except Exception as e:
            raise PersistenciaException(f"Error al leer: {str(e)}", nombre_archivo)

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION


class TierraService:
    """Servicio para gestionar operaciones sobre tierras.

    Proporciona funcionalidad para crear tierras con sus plantaciones asociadas,
    estableciendo correctamente la relación bidireccional entre ambas entidades.
    """

    def crear_tierra_con_plantacion(self, id_padron_catastral: int, superficie: float,
                                    domicilio: str, nombre_plantacion: str) -> Tierra:
        """Crea una tierra con una plantación asociada.

        Crea una instancia de Tierra y una de Plantación con la misma superficie,
        estableciendo la relación bidireccional entre ambas. La plantación se
        inicializa con la cantidad de agua configurada en las constantes.

        Argumentos:
            id_padron_catastral (int): Identificador único del padrón catastral.
            superficie (float): Superficie de la tierra en metros cuadrados.
                La plantación tendrá la misma superficie.
            domicilio (str): Dirección o ubicación de la tierra.
            nombre_plantacion (str): Nombre identificatorio de la plantación.

        Retorna:
            Tierra: Instancia de tierra creada con su plantación asociada.

        Raises:
            ValueError: Si la superficie es menor o igual a cero (validación en Tierra).
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        plantacion = Plantacion(nombre_plantacion, superficie, AGUA_INICIAL_PLANTACION)
        plantacion.set_tierra(tierra)
        tierra.set_finca(plantacion)

        print(f"Tierra creada: {domicilio} con plantacion: {nombre_plantacion}")
        return tierra

