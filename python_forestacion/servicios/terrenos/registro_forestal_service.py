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