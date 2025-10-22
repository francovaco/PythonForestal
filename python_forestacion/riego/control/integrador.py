"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/control
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/control/__init__.py
# ================================================================================

from .control_riego_task import ControlRiegoTask

__all__ = [
    'ControlRiegoTask'
]

# ================================================================================
# ARCHIVO 2/2: control_riego_task.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/riego/control/control_riego_task.py
# ================================================================================

import threading
import time
from typing import TYPE_CHECKING
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)

if TYPE_CHECKING:
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService


class ControlRiegoTask(threading.Thread, Observer[float]):
    """Controlador automático de riego que ejecuta en un hilo separado.

    Implementa el patrón Observer para recibir actualizaciones de los sensores
    de temperatura y humedad. Activa el riego automáticamente cuando las
    condiciones son adecuadas.

    El riego se activa si:
    - La temperatura está en el rango [TEMP_MIN_RIEGO, TEMP_MAX_RIEGO]
    - La humedad es menor a HUMEDAD_MAX_RIEGO

    Atributos:
        _sensor_temperatura (TemperaturaReaderTask): Sensor de temperatura observado.
        _sensor_humedad (HumedadReaderTask): Sensor de humedad observado.
        _plantacion (Plantacion): Plantación a regar.
        _plantacion_service (PlantacionService): Servicio para ejecutar el riego.
        _detenido (threading.Event): Event para detener el thread de forma segura.
        _ultima_temperatura (float): Última temperatura leída.
        _ultima_humedad (float): Última humedad leída.
    """

    def __init__(self, sensor_temperatura: 'TemperaturaReaderTask',
                 sensor_humedad: 'HumedadReaderTask',
                 plantacion: 'Plantacion',
                 plantacion_service: 'PlantacionService'):
        """Inicializa el controlador de riego.

        Se registra como observador de ambos sensores.

        Argumentos:
            sensor_temperatura (TemperaturaReaderTask): Sensor de temperatura.
            sensor_humedad (HumedadReaderTask): Sensor de humedad.
            plantacion (Plantacion): Plantación a controlar.
            plantacion_service (PlantacionService): Servicio para operaciones de riego.
        """
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()
        self._ultima_temperatura = 0.0
        self._ultima_humedad = 0.0

        self._sensor_temperatura.agregar_observador(self)
        self._sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """Recibe notificaciones de los sensores (método del patrón Observer).

        Argumentos:
            evento (float): Valor leído por el sensor (temperatura o humedad).
        """
        pass

    def run(self) -> None:
        """Ejecuta el ciclo principal del controlador de riego.

        Evalúa periódicamente las condiciones de temperatura y humedad.
        Activa el riego si se cumplen las condiciones. Se detiene automáticamente
        si se agota el agua.
        """
        while not self._detenido.is_set():
            try:
                if (TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO and
                        self._ultima_humedad < HUMEDAD_MAX_RIEGO):
                    self._plantacion_service.regar(self._plantacion)

                time.sleep(INTERVALO_CONTROL_RIEGO)
            except AguaAgotadaException as e:
                print(f"\n{e.get_full_message()}")
                print("Sistema de riego detenido automaticamente por falta de agua.")
                break

    def detener(self) -> None:
        """Detiene el thread del controlador de forma segura.

        Establece el flag de detenido para que el ciclo run() termine.
        """
        self._detenido.set()

