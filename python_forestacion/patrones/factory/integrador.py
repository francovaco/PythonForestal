"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/factory
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/factory/__init__.py
# ================================================================================

from .cultivo_factory import CultivoFactory

__all__ = [
    'CultivoFactory'
]

# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/factory/cultivo_factory.py
# ================================================================================

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """Fábrica para la creación de instancias de cultivos.

    Implementa el patrón Factory Method para desacoplar la creación de objetos
    de cultivo del código cliente. Permite crear diferentes tipos de cultivos
    sin que el cliente conozca las clases concretas.

    Este patrón facilita la extensibilidad del sistema al agregar nuevos tipos
    de cultivos sin modificar el código existente.
    """

    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """Crea una instancia de cultivo según la especie especificada.

        Argumentos:
            especie (str): Nombre de la especie del cultivo a crear.
                Valores válidos: "Pino", "Olivo", "Lechuga", "Zanahoria".

        Retorna:
            Cultivo: Instancia del tipo de cultivo solicitado.

        Raises:
            ValueError: Si la especie especificada no está registrada en la fábrica.
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> 'Cultivo':
        """Crea una instancia de Pino con configuración por defecto.

        Retorna:
            Cultivo: Instancia de Pino con variedad "Parana".
        """
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")

    @staticmethod
    def _crear_olivo() -> 'Cultivo':
        """Crea una instancia de Olivo con configuración por defecto.

        Retorna:
            Cultivo: Instancia de Olivo con tipo de aceituna ARBEQUINA.
        """
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> 'Cultivo':
        """Crea una instancia de Lechuga con configuración por defecto.

        Retorna:
            Cultivo: Instancia de Lechuga con variedad "Crespa".
        """
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Crespa")

    @staticmethod
    def _crear_zanahoria() -> 'Cultivo':
        """Crea una instancia de Zanahoria con configuración por defecto.

        Retorna:
            Cultivo: Instancia de Zanahoria tipo baby carrot.
        """
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(is_baby_carrot=True)

