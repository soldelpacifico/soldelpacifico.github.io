from django.db import models
from datetime import datetime

class Noticia(models.Model):
    fecha_Publicacion = models.DateTimeField(blank=True, null=True)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='sol/noticias',blank=True,null=True)

    def publish(self):
        self.fecha_Publicacion = datetime.today
        self.save()

    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    pregunta=models.TextField()
    respuesta=models.TextField(blank=True,null=True)
    respondida=models.BooleanField()
    
    def __str__(self):
        return self.pregunta

class Aviso(models.Model):
    dia=models.DateTimeField()
    titulo=models.CharField(max_length=30)
    mensaje=models.TextField()

    def publish(self):
        self.dia = datetime.today
        self.save()

    def __str__(self):
        return self.mensaje