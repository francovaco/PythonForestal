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