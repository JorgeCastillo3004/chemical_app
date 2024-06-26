# Generated by Django 5.0.2 on 2024-02-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pregunta',
            old_name='a',
            new_name='opcion_a',
        ),
        migrations.RenameField(
            model_name='pregunta',
            old_name='b',
            new_name='opcion_b',
        ),
        migrations.RenameField(
            model_name='pregunta',
            old_name='c',
            new_name='opcion_c',
        ),
        migrations.RenameField(
            model_name='pregunta',
            old_name='d',
            new_name='opcion_d',
        ),
        migrations.RenameField(
            model_name='pregunta',
            old_name='correcta',
            new_name='respuesta_correcta',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='explicacion',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='pregunta',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='nivel_dificultad',
            field=models.CharField(choices=[('facil', 'Facil'), ('intermedio', 'Intermedio'), ('dificil', 'Dificil')], default='facil', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pregunta',
            name='pregunta_text',
            field=models.CharField(default='facil', max_length=200),
            preserve_default=False,
        ),
    ]
