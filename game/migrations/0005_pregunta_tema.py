# Generated by Django 5.0.2 on 2024-03-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='tema',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]