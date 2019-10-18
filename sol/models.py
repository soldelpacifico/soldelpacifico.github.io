from django.db import models
from django.utils import timezone

class Noticia(models.Model):
    fecha_Publicacion = models.DateTimeField(blank=True, null=True)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def publish(self):
        self.fecha_Publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    nombre=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    pregunta=models.TextField()
    respuesta=models.TextField(blank=True, null=True)
    respondida=models.BooleanField()

    def publish(self):
        self.respondida = True
        self.save()
    
    def __str__(self):
        return self.pregunta