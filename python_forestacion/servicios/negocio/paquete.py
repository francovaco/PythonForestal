from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """Contenedor genérico para empaquetar ítems del mismo tipo.

    Implementa un paquete o caja genérica que puede contener múltiples ítems
    de un tipo específico. Utiliza TypeVar para proporcionar type-safety en
    tiempo de desarrollo. Cada paquete tiene un ID único generado mediante
    un contador de clase.

    Atributos:
        _contador_id (int): Contador de clase para generar IDs únicos.
        _id (int): Identificador único del paquete.
        _items (List[T]): Lista de ítems contenidos en el paquete.

    Tipo de parámetros:
        T: Tipo de ítems que contendrá el paquete (ej: Lechuga, Pino, Olivo).

    Ejemplos:
        >>> paquete_lechugas = Paquete[Lechuga]()
        >>> paquete_lechugas.agregar_item(lechuga1)
        >>> paquete_lechugas.mostrar_contenido_caja()
    """

    _contador_id = 0

    def __init__(self):
        """Inicializa un nuevo paquete vacío con ID único.

        El ID se genera automáticamente incrementando el contador de clase,
        garantizando que cada paquete tenga un identificador único en el sistema.
        """
        Paquete._contador_id += 1
        self._id = Paquete._contador_id
        self._items: List[T] = []

    def agregar_item(self, item: T) -> None:
        """Agrega un ítem al paquete.

        Argumentos:
            item (T): Ítem a agregar al paquete. Debe ser del tipo especificado
                en el genérico del paquete.
        """
        self._items.append(item)

    def get_items(self) -> List[T]:
        """Obtiene una copia de la lista de ítems del paquete.

        Retorna una copia para evitar modificaciones externas de la lista interna.

        Retorna:
            List[T]: Copia de la lista de ítems contenidos en el paquete.
        """
        return self._items.copy()

    def mostrar_contenido_caja(self) -> None:
        """Muestra por consola el contenido del paquete.

        Imprime información resumida del paquete incluyendo el tipo de ítems,
        la cantidad y el ID del paquete. Si el paquete está vacío, lo indica.
        """
        print("\nContenido de la caja:")
        if self._items:
            print(f"  Tipo: {self._items[0].__class__.__name__}")
            print(f"  Cantidad: {len(self._items)}")
            print(f"  ID Paquete: {self._id}")
        else:
            print("  (vacia)")