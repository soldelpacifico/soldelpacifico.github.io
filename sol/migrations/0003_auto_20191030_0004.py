# Generated by Django 2.2.3 on 2019-10-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol', '0002_pregunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='respondida',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='respuesta',
            field=models.TextField(blank=True, null=True),
        ),
    ]