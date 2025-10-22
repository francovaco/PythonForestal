"""Sistema de Gestión Forestal - Aplicación Principal.

Este módulo contiene el punto de entrada principal del sistema de gestión forestal.
Demuestra la implementación de los patrones de diseño Singleton, Factory, Observer
y Strategy en un contexto de gestión de plantaciones y cultivos.

El sistema incluye:
- Gestión de tierras y plantaciones
- Creación de cultivos usando Factory Method
- Sistema de riego automatizado con patrón Observer
- Persistencia de datos
- Manejo de trabajadores y tareas
"""

import sys
from datetime import date
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT

from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.negocio.fincas_service import FincasService

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.pino import Pino

from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

from python_forestacion.excepciones import (
    SuperficieInsuficienteException,
    AguaAgotadaException,
    PersistenciaException
)


def main():
    """Función principal del sistema de gestión forestal.

    Ejecuta una demostración completa del sistema incluyendo:
    1. Inicialización de servicios con patrón Singleton
    2. Creación de tierras y plantaciones
    3. Plantación de cultivos usando Factory Method
    4. Sistema de riego automatizado con patrón Observer
    5. Gestión de trabajadores y tareas
    6. Persistencia de registros forestales
    7. Operaciones de negocio con paquetes

    El sistema maneja excepciones específicas del dominio y asegura
    una limpieza adecuada de recursos al finalizar.
    """
    try:
        print("=" * 70)
        print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
        print("=" * 70)

        print("\n" + "-" * 70)
        print("  PATRON SINGLETON: Inicializando servicios")
        print("-" * 70)

        registry = CultivoServiceRegistry.get_instance()
        registry2 = CultivoServiceRegistry.get_instance()

        if registry is registry2:
            print("[OK] Todos los servicios comparten la misma instancia del Registry")
        else:
            print("[ERROR] Singleton no funciona correctamente")
            return

        tierra_service = TierraService()
        plantacion_service = PlantacionService(registry)
        registro_service = RegistroForestalService(registry)
        trabajador_service = TrabajadorService()
        fincas_service = FincasService(plantacion_service, registry)

        print("\n1. Creando tierra con plantacion...")
        terreno = tierra_service.crear_tierra_con_plantacion(
            id_padron_catastral=1,
            superficie=10000.0,
            domicilio="Agrelo, Mendoza",
            nombre_plantacion="Finca del Madero"
        )
        plantacion = terreno.get_finca()

        print("\n2. Creando registro forestal...")
        registro = RegistroForestal(
            id_padron=1,
            tierra=terreno,
            plantacion=plantacion,
            propietario="Juan Perez",
            avaluo=50309233.55
        )
        print(f"   Registro creado para: {registro.get_propietario()}")

        print("\n" + "-" * 70)
        print("  PATRON FACTORY: Plantando cultivos")
        print("-" * 70)

        print("\n3. Plantando cultivos usando Factory Method...")
        plantacion_service.plantar(plantacion, "Pino", 5)
        plantacion_service.plantar(plantacion, "Olivo", 5)
        plantacion_service.plantar(plantacion, "Lechuga", 5)
        plantacion_service.plantar(plantacion, "Zanahoria", 5)

        print(f"\n   Total cultivos plantados: {len(plantacion.get_cultivos())}")

        print("\n" + "-" * 70)
        print("  PATRON OBSERVER: Sistema de riego automatizado")
        print("-" * 70)

        print("\n4. Iniciando sistema de riego...")
        print("   (Sensores notificaran eventos automaticamente)")

        tarea_temp = TemperaturaReaderTask()
        tarea_hum = HumedadReaderTask()
        tarea_control = ControlRiegoTask(
            tarea_temp,
            tarea_hum,
            plantacion,
            plantacion_service
        )

        tarea_temp.start()
        tarea_hum.start()
        tarea_control.start()

        print("\n5. Gestionando trabajadores...")

        tareas = [
            Tarea(1, date.today(), "Desmalezar"),
            Tarea(2, date.today(), "Abonar"),
            Tarea(3, date.today(), "Marcar surcos")
        ]

        trabajador = Trabajador(
            dni=43888734,
            nombre="Juan Perez",
            tareas=tareas
        )

        plantacion.set_trabajadores([trabajador])

        trabajador_service.asignar_apto_medico(
            trabajador,
            apto=True,
            fecha_emision=date.today(),
            observaciones="Estado de salud: excelente"
        )

        print("\n6. Ejecutando tareas del trabajador...")
        herramienta = Herramienta(1, "Pala", True)
        trabajador_service.trabajar(trabajador, date.today(), herramienta)

        print("\n" + "-" * 70)
        print("  PATRON STRATEGY: Absorcion de agua diferenciada")
        print("-" * 70)

        print("\n7. Sistema de riego ejecutandose por 20 segundos...")
        print("   (Arboles usan estrategia estacional, Hortalizas constante)")

        import time
        time.sleep(20)

        tarea_temp.detener()
        tarea_hum.detener()
        tarea_control.detener()

        tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)
        tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
        tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)

        print("\n   Sistema de riego detenido correctamente")

        print("\n8. Operaciones de fincas...")
        fincas_service.add_finca(registro)
        fincas_service.fumigar(1, "insecticida organico")

        print("\n9. Cosechando cultivos...")
        caja_lechugas = fincas_service.cosechar_yempaquetar(Lechuga)
        caja_lechugas.mostrar_contenido_caja()

        caja_pinos = fincas_service.cosechar_yempaquetar(Pino)
        caja_pinos.mostrar_contenido_caja()

        print("\n10. Persistiendo registro en disco...")
        registro_service.persistir(registro)

        print("\n11. Leyendo registro desde disco...")
        registro_leido = RegistroForestalService.leer_registro("Juan Perez")
        registro_service.mostrar_datos(registro_leido)

        print("\n" + "=" * 70)
        print("              EJEMPLO COMPLETADO EXITOSAMENTE")
        print("=" * 70)
        print("\n  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
        print("  [OK] FACTORY     - Creacion de cultivos")
        print("  [OK] OBSERVER    - Sistema de sensores y eventos")
        print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
        print("=" * 70)
        print()

    except SuperficieInsuficienteException as e:
        print(f"\n[ERROR] {e.get_full_message()}")
        print(f"   Tipo de cultivo: {e.get_tipo_cultivo()}")
        print(f"   Superficie requerida: {e.get_superficie_requerida():.2f} m²")
        print(f"   Superficie disponible: {e.get_superficie_disponible():.2f} m²")
        sys.exit(1)

    except AguaAgotadaException as e:
        print(f"\n[ERROR] {e.get_full_message()}")
        print(f"   Agua disponible: {e.get_agua_disponible()}L")
        print(f"   Agua minima: {e.get_agua_minima()}L")
        sys.exit(1)

    except PersistenciaException as e:
        print(f"\n[ERROR] {e.get_full_message()}")
        print(f"   Archivo: {e.get_nombre_archivo()}")
        sys.exit(1)

    except Exception as e:
        print(f"\n[ERROR INESPERADO] {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()