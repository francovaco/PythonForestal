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