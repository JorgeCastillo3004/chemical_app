from django.shortcuts import render

# Create your views here.
def quices(request):
    """
    Vista para la página de inicio de la aplicación.
    """
    # Aquí puedes escribir el código para recuperar los datos necesarios de la base de datos
    # y pasarlos al contexto para su renderización en la plantilla.
    # time_data = TimeDeltaData.objects.all()
    context = {'Take_test':'Take_test'}
    return render(request, 'quices/home_quices.html', context)