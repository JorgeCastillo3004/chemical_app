from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import PreguntaForm
from .models import Pregunta
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect


def game(request):
    """
    Vista para la página de inicio de la aplicación.
    """
    # Aquí puedes escribir el código para recuperar los datos necesarios de la base de datos
    # y pasarlos al contexto para su renderización en la plantilla.
    # time_data = TimeDeltaData.objects.all()
    context = {'Start_play':'Start_play'}
    return render(request, 'game/home_game.html', context)

# def camino_actividades(request):
#     """
#     Vista para la página de inicio de la aplicación.
#     """
#     # Aquí puedes escribir el código para recuperar los datos necesarios de la base de datos
#     # y pasarlos al contexto para su renderización en la plantilla.
#     # time_data = TimeDeltaData.objects.all()
#     # context = {
#     #     'time_data': time_data,
#     # }
#     context = {'Start_play':'Start_play'}
#     return render(request, 'game/camino_actividades.html', context)

def camino_temas(request):
    temas = Pregunta.objects.values_list('tema', flat=True).distinct()
    return render(request, 'game/camino_temas.html', {'temas': temas})    

def preguntas_por_tema(request, tema):
    temas = Pregunta.objects.values_list('tema', flat=True).distinct()
    return render(request, 'game/preguntas_por_tema.html', {'tema': tema})

def actividad_interactiva(request):
    """
    Vista para la página de inicio de la aplicación.
    """
    # Aquí puedes escribir el código para recuperar los datos necesarios de la base de datos
    # y pasarlos al contexto para su renderización en la plantilla.
    # time_data = TimeDeltaData.objects.all()
    # context = {
    #     'time_data': time_data,
    # }
    context = {'Start_play':'Start_play'}
    return render(request, 'game/actividad_interactiva.html', context)

def crear_pregunta(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pregunta_creada_exitosamente')  # Redirigir a una página de éxito
    else:
        form = PreguntaForm()
    return render(request, 'game/crear_pregunta.html', {'form': form})

def pregunta_creada_exitosamente(request):
    return render(request, 'game/pregunta_creada_exitosamente.html')

def mostrar_preguntas(request, tema, numero_pregunta):
    preguntas = Pregunta.objects.filter(tema=tema)
    total_preguntas = len(preguntas)

    print(f"Pregunta actual: {numero_pregunta}/{total_preguntas}")

    if numero_pregunta <= total_preguntas:
        pregunta = preguntas[numero_pregunta - 1]
        return render(request, 'game/mostrar_preguntas.html', {'pregunta': pregunta, 'total_preguntas': total_preguntas})
    else:
        print("Caso finalización de preguntas")
        return HttpResponseRedirect('/game/mensaje_felicitaciones/' + tema + '/')

def mensaje_felicitaciones(request, tema):
	mensaje = f"Felicitaciones, has logrado finalizar las preguntas relacionadas al tema {tema}. Espero que sigas motivado y trabajando en los siguientes temas. ¡Felicitaciones!"
	return render(request, 'game/mensaje_felicitaciones.html', {'mensaje': mensaje})
# def siguiente_pregunta(request):
#     # Obtener el id de la última pregunta mostrada
#     ultima_pregunta_id = request.GET.get('ultima_pregunta_id', None)

#     # Obtener la siguiente pregunta
#     siguiente_pregunta = Pregunta.objects.filter(id__gt=ultima_pregunta_id).first()

#     if siguiente_pregunta:
#         # Renderizar la plantilla de pregunta con la siguiente pregunta
#         return render(request, 'game/mostrar_preguntas.html', {'tema': siguiente_pregunta.tema, 'pregunta_actual':pregunta.id})
#     else:
#         # No hay más preguntas disponibles
#         return JsonResponse({'mensaje': 'No hay más preguntas disponibles.'})

def corregir_respuesta(request):
    if request.method == 'POST':
        pregunta_id = request.POST.get('pregunta_id')
        opcion_seleccionada = request.POST.get('opcion')
        pregunta = Pregunta.objects.get(id=pregunta_id)
        if opcion_seleccionada == pregunta.respuesta_correcta:
            correcta = True
        else:
            correcta = False
        print("Pregunta id sent: ", pregunta.id, type(pregunta.id))
        return render(request, 'game/correccion.html', {'correcta': correcta,
         'respuesta_correcta': pregunta.respuesta_correcta,
          'explicacion': pregunta.explicacion, 'tema': pregunta.tema, 'pregunta_id': pregunta.id})
    else:
        return JsonResponse({'error': 'Método no permitido'})

def procesar_respuesta(request):
    if request.method == 'POST':
        pregunta_id = request.POST['pregunta_id']
        opcion_seleccionada = request.POST['opcion']
        pregunta = Pregunta.objects.get(id=pregunta_id)
        if opcion_seleccionada == pregunta.respuesta_correcta:
            mensaje = '¡Respuesta correcta!'
        else:
            mensaje = 'Respuesta incorrecta. La respuesta correcta es: ' + pregunta.respuesta_correcta
        return HttpResponse(mensaje)
    else:
        return HttpResponse('Método no permitido')

def actividad(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'game/actividad.html', {'preguntas': preguntas})

def verificar_respuesta(request, pregunta_id):
    pregunta = Pregunta.objects.get(pk=pregunta_id)
    respuesta_usuario = request.POST['respuesta']
    if respuesta_usuario == pregunta.respuesta_correcta:
        mensaje = "¡Felicitaciones! Respuesta correcta."
    else:
        mensaje = f"Incorrecto. La respuesta correcta es: {pregunta.respuesta_correcta}. {pregunta.explicacion}"
    return render(request, 'game/respuesta.html', {'mensaje': mensaje})
