from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


class ShowHistory(CreateView):
    # form_class = UserCreationForm
    # success_url = reverse_lazy("login")
    template_name = "charts/show_user_data.html"


from .models import TimeDeltaData

def index(request):
    """
    Vista para la página de inicio de la aplicación.
    """
    # Aquí puedes escribir el código para recuperar los datos necesarios de la base de datos
    # y pasarlos al contexto para su renderización en la plantilla.
    time_data = TimeDeltaData.objects.all()
    context = {
        'time_data': time_data,
    }
    return render(request, 'charts/show_user_data.html', context)


def show_results(request):
    """
    Vista para la página de inicio de la aplicación.
    """
    # Aquí puedes escribir el código para recuperar los datos necesarios de la base de datos
    # y pasarlos al contexto para su renderización en la plantilla.
    time_data = TimeDeltaData.objects.all()
    context = {
        'time_data': time_data,
    }
    return render(request, 'charts/show_results.html', context)
