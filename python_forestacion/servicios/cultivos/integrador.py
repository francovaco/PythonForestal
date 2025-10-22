"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================

from .cultivo_service import CultivoService
from .arbol_service import ArbolService
from .pino_service import PinoService
from .olivo_service import OlivoService
from .lechuga_service import LechugaService
from .zanahoria_service import ZanahoriaService
from .cultivo_service_registry import CultivoServiceRegistry

__all__ = [
    'CultivoService',
    'ArbolService',
    'PinoService',
    'OlivoService',
    'LechugaService',
    'ZanahoriaService',
    'CultivoServiceRegistry'
]

# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

from typing import TYPE_CHECKING
from .cultivo_service import CultivoService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """Servicio para operaciones específicas con árboles.

    Extiende CultivoService agregando funcionalidad específica para árboles
    como el crecimiento en altura.
    """

    def crecer(self, arbol: 'Arbol', incremento: float) -> None:
        """Aumenta la altura del árbol.

        Argumentos:
            arbol (Arbol): Árbol que crecerá.
            incremento (float): Incremento de altura en metros. Debe ser positivo.
        """
        if incremento > 0:
            arbol.set_altura(arbol.get_altura() + incremento)

# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

from threading import Lock
from typing import TYPE_CHECKING, Dict, Type

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoServiceRegistry:
    """Registro centralizado de servicios para diferentes tipos de cultivos.

    Implementa el patrón Singleton para garantizar una única instancia del registro.
    Usa thread-safe double-checked locking para la inicialización.

    Este registro actúa como un dispatcher que delega las operaciones a los
    servicios específicos según el tipo de cultivo, evitando el uso de
    condicionales if/elif en el código cliente.

    Atributos:
        _instance (CultivoServiceRegistry): Instancia única del singleton.
        _lock (Lock): Lock para garantizar thread-safety en la creación.
        _initialized (bool): Indica si la instancia ya fue inicializada.
        _pino_service (PinoService): Servicio para pinos.
        _olivo_service (OlivoService): Servicio para olivos.
        _lechuga_service (LechugaService): Servicio para lechugas.
        _zanahoria_service (ZanahoriaService): Servicio para zanahorias.
        _absorber_agua_handlers (Dict): Mapeo de tipos a métodos de absorción.
        _mostrar_datos_handlers (Dict): Mapeo de tipos a métodos de visualización.
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        """Crea o retorna la instancia única del singleton.

        Usa double-checked locking para garantizar thread-safety sin
        afectar el rendimiento después de la primera creación.

        Retorna:
            CultivoServiceRegistry: Instancia única del registro.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Inicializa el registro con todos los servicios y handlers.

        Solo se ejecuta una vez gracias al flag _initialized.
        Registra los servicios y configura los mapeos de tipos a métodos.
        """
        if self._initialized:
            return

        from .pino_service import PinoService
        from .olivo_service import OlivoService
        from .lechuga_service import LechugaService
        from .zanahoria_service import ZanahoriaService
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        self._absorber_agua_handlers: Dict[Type, any] = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        self._mostrar_datos_handlers: Dict[Type, any] = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

        self._initialized = True

    @classmethod
    def get_instance(cls):
        """Obtiene la instancia única del registro.

        Retorna:
            CultivoServiceRegistry: Instancia única del singleton.
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """Delega la operación de absorción de agua al servicio apropiado.

        Argumentos:
            cultivo (Cultivo): Cultivo que absorberá agua.

        Retorna:
            int: Cantidad de agua absorbida en litros.

        Raises:
            ValueError: Si el tipo de cultivo no está registrado.
        """
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo)

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """Delega la operación de mostrar datos al servicio apropiado.

        Argumentos:
            cultivo (Cultivo): Cultivo del cual mostrar información.

        Raises:
            ValueError: Si el tipo de cultivo no está registrado.
        """
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        self._mostrar_datos_handlers[tipo](cultivo)

    def _absorber_agua_pino(self, cultivo):
        """Handler privado para absorción de agua en pinos."""
        return self._pino_service.absorver_agua(cultivo)

    def _absorber_agua_olivo(self, cultivo):
        """Handler privado para absorción de agua en olivos."""
        return self._olivo_service.absorver_agua(cultivo)

    def _absorber_agua_lechuga(self, cultivo):
        """Handler privado para absorción de agua en lechugas."""
        return self._lechuga_service.absorver_agua(cultivo)

    def _absorber_agua_zanahoria(self, cultivo):
        """Handler privado para absorción de agua en zanahorias."""
        return self._zanahoria_service.absorver_agua(cultivo)

    def _mostrar_datos_pino(self, cultivo):
        """Handler privado para mostrar datos de pinos."""
        self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo):
        """Handler privado para mostrar datos de olivos."""
        self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo):
        """Handler privado para mostrar datos de lechugas."""
        self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo):
        """Handler privado para mostrar datos de zanahorias."""
        self._zanahoria_service.mostrar_datos(cultivo)

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

from typing import TYPE_CHECKING
from .arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """Servicio específico para operaciones con olivos.

    Extiende ArbolService usando estrategia de absorción estacional.
    Los olivos crecen automáticamente cada vez que absorben agua.
    """

    def __init__(self):
        """Inicializa el servicio con estrategia de absorción estacional."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, olivo: 'Olivo') -> int:
        """Absorbe agua y hace crecer el olivo automáticamente.

        Argumentos:
            olivo (Olivo): Olivo que absorberá agua.

        Retorna:
            int: Cantidad de agua absorbida en litros.
        """
        agua_absorvida = super().absorver_agua(olivo)
        self.crecer(olivo, CRECIMIENTO_OLIVO_POR_RIEGO)
        return agua_absorvida

    def mostrar_datos(self, olivo: 'Olivo') -> None:
        """Muestra información detallada del olivo por consola.

        Argumentos:
            olivo (Olivo): Olivo del cual mostrar información.
        """
        print(f"Cultivo: Olivo")
        print(f"Superficie: {olivo.get_superficie()} m²")
        print(f"Agua almacenada: {olivo.get_agua()} L")
        print(f"ID: {olivo.get_id()}")
        print(f"Altura: {olivo.get_altura()} m")
        print(f"Tipo de aceituna: {olivo.get_tipo().name}")

# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

### ARCHIVO: python_forestacion/servicios/cultivos/pino_service.py

from typing import TYPE_CHECKING
from .arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO_POR_RIEGO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """Servicio específico para operaciones con pinos.

    Extiende ArbolService usando estrategia de absorción estacional.
    Los pinos crecen automáticamente cada vez que absorben agua.
    """

    def __init__(self):
        """Inicializa el servicio con estrategia de absorción estacional."""
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, pino: 'Pino') -> int:
        """Absorbe agua y hace crecer el pino automáticamente.

        Argumentos:
            pino (Pino): Pino que absorberá agua.

        Retorna:
            int: Cantidad de agua absorbida en litros.
        """
        agua_absorvida = super().absorver_agua(pino)
        self.crecer(pino, CRECIMIENTO_PINO_POR_RIEGO)
        return agua_absorvida

    def mostrar_datos(self, pino: 'Pino') -> None:
        """Muestra información detallada del pino por consola.

        Argumentos:
            pino (Pino): Pino del cual mostrar información.
        """
        print(f"Cultivo: Pino")
        print(f"Superficie: {pino.get_superficie()} m²")
        print(f"Agua almacenada: {pino.get_agua()} L")
        print(f"ID: {pino.get_id()}")
        print(f"Altura: {pino.get_altura()} m")
        print(f"Variedad: {pino.get_variedad()}")

# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

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

