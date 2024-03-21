from django.urls import path
from . import views



urlpatterns = [
    path("", views.game, name='game'),
    path("camino-temas", views.camino_temas, name='camino_temas'),
    path("interactiva", views.actividad_interactiva, name='actividad_interactiva'),
    path('crear-pregunta/', views.crear_pregunta, name='crear_pregunta'),
    path('pregunta-creada-exitosamente/', views.pregunta_creada_exitosamente, name='pregunta_creada_exitosamente'),
    path('mostrar-preguntas/', views.mostrar_preguntas, name='mostrar_preguntas'),
    path('actividad/', views.actividad, name='actividad'),
    path('verificar/<int:pregunta_id>/', views.verificar_respuesta, name='verificar_respuesta'),    
    path('mostrar_preguntas/<str:tema>/<int:numero_pregunta>/', views.mostrar_preguntas, name='mostrar_preguntas'),
    path('mensaje_felicitaciones/<str:tema>/', views.mensaje_felicitaciones, name='mensaje_felicitaciones'),
    # path('siguiente_pregunta/', views.siguiente_pregunta, name='siguiente_pregunta'),
    path('corregir_respuesta/', views.corregir_respuesta, name='corregir_respuesta'),



]