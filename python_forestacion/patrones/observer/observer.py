from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """Interfaz abstracta para implementar el patrón Observer.

    Define el contrato que deben cumplir todos los observadores para
    recibir notificaciones de objetos Observable. Usa genéricos para
    proporcionar type-safety.

    Type Parameters:
        T: Tipo de evento que el observador puede procesar.
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Procesa una notificación del objeto observable.

        Argumentos:
            evento (T): Evento recibido del observable que contiene
                información sobre el cambio de estado.
        """
        pass