from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, Pregunta
from django.utils import timezone
from .forms import PreguntaForm, RespuestaForm

def index(request):
    Noticias = Noticia.objects.filter(fecha_Publicacion__lte=timezone.now()).order_by('-fecha_Publicacion')[:3]
    return render(request, 'sol/index.html', {"Noticias":Noticias})

def rutas(request):
    return render(request, 'sol/rutas.html', {})

def tarifas(request):

    return render(request, 'sol/tarifas.html', {})

def beneficios(request):
    return render(request, 'sol/beneficios.html', {})

def pertenencias(request):
    return render(request, 'sol/pertenencias.html', {})

def historia(request):
    return render(request, 'sol/historia.html', {})

def preguntas(request):
    Preguntas = Pregunta.objects.filter(respondida=True)
    return render(request, 'sol/preguntas.html', {"Preguntas":Preguntas})

def resp_preguntas(request):
    Preguntas = Pregunta.objects.filter(respondida=False)
    return render(request, 'sol/resp_preguntas.html', {"Preguntas":Preguntas})

def pregunta_new(request):
    if request.method == "POST":
        form = PreguntaForm(request.POST)
        if form.is_valid():
            Pregunta = form.save(commit=False)
            Pregunta.respuesta=""
            Pregunta.respondida = False
            Pregunta.save()
            messages.success(request,'¡Pregunta enviada exitosamente!')
            return redirect('preguntas')
    else:
        form = PreguntaForm()
    return render(request, 'sol/new_pregunta.html', {'form':form})

def pregunta_responder(request, pk):
    pregunta = get_object_or_404(Pregunta, pk=pk)
    if request.method == "POST":
        form = RespuestaForm(request.POST, instance=pregunta)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.respondida = True
            pregunta.save()
            return redirect('respPreguntas')
    else:
        form = RespuestaForm(instance=pregunta)
    return render(request, 'sol/pregunta_responder.html', {'form':form,'pregunta':pregunta})