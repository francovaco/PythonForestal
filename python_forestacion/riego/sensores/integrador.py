"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/sensores
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/sensores/__init__.py
# ================================================================================

from .temperatura_reader_task import TemperaturaReaderTask
from .humedad_reader_task import HumedadReaderTask

__all__ = [
    'TemperaturaReaderTask',
    'HumedadReaderTask'
]

# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ================================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX
)


class HumedadReaderTask(threading.Thread, Observable[float]):
    """Tarea que simula un sensor de humedad en un hilo separado.

    Implementa el patrón Observer como Observable, notificando a los observadores
    cada vez que lee un nuevo valor de humedad. Ejecuta en un thread daemon.

    La humedad se genera aleatoriamente dentro de un rango configurable.

    Atributos:
        _detenido (threading.Event): Event para detener el thread de forma segura.
    """

    def __init__(self):
        """Inicializa el sensor de humedad como thread daemon y observable."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Ejecuta el ciclo principal del sensor.

        Lee la humedad periódicamente, la imprime y notifica a los observadores.
        Continúa hasta que se invoque detener().
        """
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            print(f"[Humedad] {humedad:.2f} %")
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)

    def _leer_humedad(self) -> float:
        """Simula la lectura de humedad del sensor.

        Retorna:
            float: Humedad aleatoria en porcentaje (0-100) dentro del rango configurado.
        """
        return SENSOR_HUMEDAD_MIN + random.random() * (SENSOR_HUMEDAD_MAX - SENSOR_HUMEDAD_MIN)

    def detener(self) -> None:
        """Detiene el thread del sensor de forma segura.

        Establece el flag de detenido para que el ciclo run() termine.
        """
        self._detenido.set()

# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ================================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)


class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """Tarea que simula un sensor de temperatura en un hilo separado.

    Implementa el patrón Observer como Observable, notificando a los observadores
    cada vez que lee una nueva temperatura. Ejecuta en un thread daemon.

    La temperatura se genera aleatoriamente dentro de un rango configurable.

    Atributos:
        _detenido (threading.Event): Event para detener el thread de forma segura.
    """

    def __init__(self):
        """Inicializa el sensor de temperatura como thread daemon y observable."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """Ejecuta el ciclo principal del sensor.

        Lee la temperatura periódicamente, la imprime y notifica a los observadores.
        Continúa hasta que se invoque detener().
        """
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            print(f"[Temperatura] {temperatura:.2f} °C")
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def _leer_temperatura(self) -> float:
        """Simula la lectura de temperatura del sensor.

        Retorna:
            float: Temperatura aleatoria en grados Celsius dentro del rango configurado.
        """
        return SENSOR_TEMP_MIN + random.random() * (SENSOR_TEMP_MAX - SENSOR_TEMP_MIN)

    def detener(self) -> None:
        """Detiene el thread del sensor de forma segura.

        Establece el flag de detenido para que el ciclo run() termine.
        """
        self._detenido.set()

