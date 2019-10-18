from django.shortcuts import render
from .models import Noticia, Pregunta
from django.utils import timezone

def index(request):
    Noticias = Noticia.objects.filter(fecha_Publicacion__lte=timezone.now()).order_by('-fecha_Publicacion')[:3]
    return render(request, 'sol/index.html', {"Noticias":Noticias})

def tarifas(request):

    return render(request, 'sol/tarifas.html', {})

def pertenencias(request):
    return render(request, 'sol/pertenencias.html', {})

def historia(request):
    return render(request, 'sol/historia.html', {})

def preguntas(request):
    Preguntas = Pregunta.objects.filter(respondida=True)
    return render(request, 'sol/preguntas.html', {"Preguntas":Preguntas})