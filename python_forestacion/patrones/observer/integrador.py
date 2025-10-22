"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/observer
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/observer/__init__.py
# ================================================================================

from .observable import Observable
from .observer import Observer

__all__ = [
    'Observable',
    'Observer'
]

# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/observer/observable.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/patrones/observer/observer.py
# ================================================================================

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

