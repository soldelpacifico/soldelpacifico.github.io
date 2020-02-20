from django.db import models
from datetime import datetime

class NoticiaTrans(models.Model):
    fecha_Publicacion = models.DateTimeField(blank=True, null=True)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='sol/noticiastrans',blank=True,null=True)

    def publish(self):
        self.fecha_Publicacion = datetime.today
        self.save()

    def __str__(self):
        return self.titulo
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
        return self.titulo

class Inicio(models.Model):
    lugar=models.CharField(max_length=30)

    def __str__(self):
        return self.lugar



class Tarifa(models.Model):
    inicio=models.ForeignKey(Inicio, on_delete=models.CASCADE)
    destino=models.CharField(max_length=60)
    valor=models.IntegerField()
    estudiante=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.destino

class Idea(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    idea=models.TextField()
    publicada=models.BooleanField()

    def __str__(self):
        return self.idea