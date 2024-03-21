from django.urls import path
from . import views




urlpatterns = [
    path("", views.index, name='charts'),
    path("results", views.show_results, name='show_results'),
]