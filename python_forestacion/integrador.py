"""
Archivo integrador generado automaticamente
Directorio: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion
Fecha: 2025-10-21 21:15:59
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: /Users/vaco/Downloads/Facultad/diseño de sistemas/PythonForestal/python_forestacion/constantes.py
# ================================================================================

"""Constantes de configuración del sistema de gestión forestal.

Este módulo centraliza todas las constantes utilizadas en el sistema,
incluyendo parámetros de cultivos, riego, sensores y persistencia.

Atributos:
    AGUA_MINIMA (int): Cantidad mínima de agua requerida en la plantación en litros.
    AGUA_INICIAL_PLANTACION (int): Agua inicial al crear una plantación en litros.

    TEMP_MIN_RIEGO (int): Temperatura mínima para activar riego en °C.
    TEMP_MAX_RIEGO (int): Temperatura máxima para activar riego en °C.
    HUMEDAD_MAX_RIEGO (int): Humedad máxima para activar riego en %.

    SUPERFICIE_PINO (float): Superficie requerida por pino en m².
    SUPERFICIE_OLIVO (float): Superficie requerida por olivo en m².
    SUPERFICIE_LECHUGA (float): Superficie requerida por lechuga en m².
    SUPERFICIE_ZANAHORIA (float): Superficie requerida por zanahoria en m².

    AGUA_INICIAL_PINO (int): Agua inicial de un pino en litros.
    AGUA_INICIAL_OLIVO (int): Agua inicial de un olivo en litros.
    AGUA_INICIAL_LECHUGA (int): Agua inicial de una lechuga en litros.
    AGUA_INICIAL_ZANAHORIA (int): Agua inicial de una zanahoria en litros.

    ALTURA_INICIAL_ARBOL (float): Altura inicial de árboles genéricos en metros.
    ALTURA_INICIAL_OLIVO (float): Altura inicial de olivos en metros.

    ABSORCION_SEASONAL_VERANO (int): Absorción de agua en verano en litros.
    ABSORCION_SEASONAL_INVIERNO (int): Absorción de agua en invierno en litros.
    ABSORCION_CONSTANTE_LECHUGA (int): Absorción constante de lechuga en litros.
    ABSORCION_CONSTANTE_ZANAHORIA (int): Absorción constante de zanahoria en litros.

    MES_INICIO_VERANO (int): Mes de inicio del verano (1-12).
    MES_FIN_VERANO (int): Mes de fin del verano (1-12).

    CRECIMIENTO_PINO_POR_RIEGO (float): Incremento de altura del pino por riego en metros.
    CRECIMIENTO_OLIVO_POR_RIEGO (float): Incremento de altura del olivo por riego en metros.

    INTERVALO_SENSOR_TEMPERATURA (float): Intervalo de lectura del sensor en segundos.
    INTERVALO_SENSOR_HUMEDAD (float): Intervalo de lectura del sensor en segundos.
    INTERVALO_CONTROL_RIEGO (float): Intervalo de evaluación del control en segundos.
    THREAD_JOIN_TIMEOUT (float): Timeout para join de threads en segundos.

    SENSOR_TEMP_MIN (int): Temperatura mínima del sensor en °C.
    SENSOR_TEMP_MAX (int): Temperatura máxima del sensor en °C.
    SENSOR_HUMEDAD_MIN (int): Humedad mínima del sensor en %.
    SENSOR_HUMEDAD_MAX (int): Humedad máxima del sensor en %.

    DIRECTORIO_DATA (str): Directorio para archivos de persistencia.
    EXTENSION_DATA (str): Extensión de archivos de datos.
"""

AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50

SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 3.0
SUPERFICIE_LECHUGA = 0.10
SUPERFICIE_ZANAHORIA = 0.15

AGUA_INICIAL_PINO = 2
AGUA_INICIAL_OLIVO = 5
AGUA_INICIAL_LECHUGA = 1
AGUA_INICIAL_ZANAHORIA = 0

ALTURA_INICIAL_ARBOL = 1.0
ALTURA_INICIAL_OLIVO = 0.5

ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
ABSORCION_CONSTANTE_LECHUGA = 1
ABSORCION_CONSTANTE_ZANAHORIA = 2

MES_INICIO_VERANO = 3
MES_FIN_VERANO = 8

CRECIMIENTO_PINO_POR_RIEGO = 0.10
CRECIMIENTO_OLIVO_POR_RIEGO = 0.01

INTERVALO_SENSOR_TEMPERATURA = 2.0
INTERVALO_SENSOR_HUMEDAD = 3.0
INTERVALO_CONTROL_RIEGO = 2.5
THREAD_JOIN_TIMEOUT = 2.0

SENSOR_TEMP_MIN = -25
SENSOR_TEMP_MAX = 50
SENSOR_HUMEDAD_MIN = 0
SENSOR_HUMEDAD_MAX = 100

DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

