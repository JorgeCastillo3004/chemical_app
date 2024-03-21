from django.urls import path
from . import views


urlpatters = [
	path("", views.quices, name = 'test'),
]