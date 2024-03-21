from django.db import models

class Pregunta(models.Model):
	pregunta_text = models.CharField(max_length=200)
	opcion_a = models.CharField(max_length=100)
	opcion_b = models.CharField(max_length=100)
	opcion_c = models.CharField(max_length=100)
	opcion_d = models.CharField(max_length=100)
	respuesta_correcta = models.CharField(max_length=1)
	explicacion = models.CharField(max_length=200)
	tema = models.CharField(max_length=80)
	nivel_dificultad = models.CharField(max_length=10, choices=[('facil', 'Facil'), ('intermedio', 'Intermedio'), ('dificil', 'Dificil')])

	def __str__(self):
		return self.pregunta_text


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)