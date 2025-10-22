from typing import Generic, TypeVar, List
from .observer import Observer

T = TypeVar('T')


class Observable(Generic[T]):
    """Clase base para implementar el patrón Observer (Observable).

    Esta clase permite que los objetos notifiquen automáticamente a sus
    observadores cuando ocurren cambios de estado. Usa genéricos para
    proporcionar type-safety en las notificaciones.

    Atributos:
        _observadores (List[Observer[T]]): Lista de observadores registrados.

    Type Parameters:
        T: Tipo de evento que se notifica a los observadores.
    """

    def __init__(self):
        """Inicializa un nuevo Observable sin observadores."""
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Registra un observador para recibir notificaciones.

        Argumentos:
            observador (Observer[T]): Observador a agregar. Si ya está registrado,
                no se agrega nuevamente.
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador de la lista de notificaciones.

        Argumentos:
            observador (Observer[T]): Observador a eliminar. Si no está registrado,
                no hace nada.
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores registrados sobre un evento.

        Argumentos:
            evento (T): Evento a notificar a los observadores.
        """
        for observador in self._observadores:
            observador.actualizar(evento)