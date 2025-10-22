from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION


class TierraService:
    """Servicio para gestionar operaciones sobre tierras.

    Proporciona funcionalidad para crear tierras con sus plantaciones asociadas,
    estableciendo correctamente la relación bidireccional entre ambas entidades.
    """

    def crear_tierra_con_plantacion(self, id_padron_catastral: int, superficie: float,
                                    domicilio: str, nombre_plantacion: str) -> Tierra:
        """Crea una tierra con una plantación asociada.

        Crea una instancia de Tierra y una de Plantación con la misma superficie,
        estableciendo la relación bidireccional entre ambas. La plantación se
        inicializa con la cantidad de agua configurada en las constantes.

        Argumentos:
            id_padron_catastral (int): Identificador único del padrón catastral.
            superficie (float): Superficie de la tierra en metros cuadrados.
                La plantación tendrá la misma superficie.
            domicilio (str): Dirección o ubicación de la tierra.
            nombre_plantacion (str): Nombre identificatorio de la plantación.

        Retorna:
            Tierra: Instancia de tierra creada con su plantación asociada.

        Raises:
            ValueError: Si la superficie es menor o igual a cero (validación en Tierra).
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        plantacion = Plantacion(nombre_plantacion, superficie, AGUA_INICIAL_PLANTACION)
        plantacion.set_tierra(tierra)
        tierra.set_finca(plantacion)

        print(f"Tierra creada: {domicilio} con plantacion: {nombre_plantacion}")
        return tierra