import os
import django
import csv
from game.models import Pregunta  # Asegúrate de importar correctamente el modelo Pregunta

# Configurar la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_educativa.settings")

# Configurar Django
django.setup()

def cargar_datos_desde_csv(ruta_archivo):
    with open(ruta_archivo, newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  # Omitir la fila de encabezado si existe
        
        for fila in lector_csv:
            # Crear una nueva instancia de Pregunta con los datos de la fila
            pregunta = Pregunta(
                pregunta_text=fila[0],  
                opcion_a=fila[1],
                opcion_b=fila[2],
                opcion_c=fila[3],
                opcion_d=fila[4],
                respuesta_correcta=fila[5],
                explicacion=fila[6],
                nivel_dificultad=fila[7]
            )
            pregunta.save()  # Guardar la instancia en la base de datos

# Llama a la función y pasa la ruta del archivo CSV
ruta_archivo_csv = 'componentes.csv'
cargar_datos_desde_csv(ruta_archivo_csv)
