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