import csv
from django.core.exceptions import ValidationError
from .forms import PreguntaForm  # Importa el formulario PreguntaForm
from .models import Pregunta  # Importa el modelo Pregunta

def cargar_datos_desde_csv(ruta_archivo):
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            form = PreguntaForm(fila)  # Crea una instancia del formulario con los datos de la fila
            if form.is_valid():
                try:
                    form.save()  # Guarda los datos en el modelo Pregunta si son válidos
                except ValidationError as e:
                    print(f"Error al guardar la fila {fila}: {e}")
            else:
                print(f"Datos inválidos en la fila {fila}: {form.errors}")

# Llama a la función y pasa la ruta del archivo CSV
ruta_archivo_csv = '/home/jorge/work/django_proyect/app_educativa/componentes.csv'
cargar_datos_desde_csv(ruta_archivo_csv)
