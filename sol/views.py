from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, Pregunta, Aviso, Inicio, Tarifa, NoticiaTrans, Idea
from django.utils import timezone
from .forms import PreguntaForm, RespuestaForm, PreguntaLogueadoForm, UserCreateForm, IdeaForm
from datetime import date

from django.core.paginator import Paginator

#Pass Recover

def error404(request, exception):
    return render(request, 'error_404.html', {})

def index(request):
    #Contenido index
    today = date.today()
    Noticias = Noticia.objects.filter(fecha_Publicacion__lte=timezone.now()).order_by('-fecha_Publicacion')[:3]
    Avisos = Aviso.objects.filter(dia__year=today.year,
                                       dia__month=today.month,
                                       dia__day=today.day)
    #Buscador de tarifas
    Inicios = Inicio.objects.all().order_by('lugar')
    Inicios_get = request.GET.get('desde')
    Destinos_get = request.GET.get('hacia')
    inicio_resultado = None
    destino_resultado = None
    Destinos = None
    cb1Selected= None
    cb2Selected= None

    if Inicios_get!='Seleccione' and Inicios_get is not None:
        inicio_resultado = Inicio.objects.filter(lugar=Inicios_get)[0]
        cb1Selected = inicio_resultado
        Destinos = Tarifa.objects.filter(inicio=inicio_resultado).order_by('destino')

    if Destinos_get!='Seleccione' and Destinos_get is not None:
        destino_resultado = Tarifa.objects.get(destino=Destinos_get, inicio=inicio_resultado)
        cb2Selected = destino_resultado
    
    contexto = {
        #ContIndex
        "Noticias":Noticias,
        "Avisos":Avisos,
        #BuscadorTarifas
        "Inicios":Inicios,
        "Destinos":Destinos,
        "cb1Selected":cb1Selected,
        "cb2Selected":cb2Selected
    }
    return render(request, 'sol/index.html', contexto)

def todasnoticias(request):
    Noticias = Noticia.objects.filter(fecha_Publicacion__lte=timezone.now()).order_by('-fecha_Publicacion')

    paginator = Paginator(Noticias, 10)

    page = request.GET.get('page')

    Noticias = paginator.get_page(page)
    return render(request, 'sol/noticias.html', {"Noticias":Noticias,"Preguntas":Noticias})


def itinerarios(request):
    return render(request, 'sol/itinerarios.html', {})

def rutas(request):
    return render(request, 'sol/rutas.html', {})

def terminales(request):
    return render(request, 'sol/terminales.html', {})

def transrural(request):
    Noticias = NoticiaTrans.objects.filter(fecha_Publicacion__lte=timezone.now()).order_by('-fecha_Publicacion')
    return render(request, 'sol/transrural.html', {"Noticias":Noticias})

def tarifas(request):
    Inicios = Inicio.objects.all().order_by('lugar')
    Inicios_get = request.GET.get('desde')
    Destinos_get = request.GET.get('hacia')
    inicio_resultado = None
    destino_resultado = None
    Destinos = None
    cb1Selected= None
    cb2Selected= None

    if Inicios_get!='Seleccione' and Inicios_get is not None:
        inicio_resultado = Inicio.objects.filter(lugar=Inicios_get)[0]
        cb1Selected = inicio_resultado
        Destinos = Tarifa.objects.filter(inicio=inicio_resultado).order_by('destino')

    if Destinos_get!='Seleccione' and Destinos_get is not None:
        destino_resultado = Tarifa.objects.get(destino=Destinos_get, inicio=inicio_resultado)
        cb2Selected = destino_resultado
    contexto = {
        "Inicios":Inicios,
        "Destinos":Destinos,
        "cb1Selected":cb1Selected,
        "cb2Selected":cb2Selected
    }
    return render(request, 'sol/tarifas.html', contexto)

def beneficios(request):
    return render(request, 'sol/beneficios.html', {})

def pertenencias(request):
    return render(request, 'sol/pertenencias.html', {})

def derechos(request):
    return render(request, 'sol/derechos.html', {})

def reclamo(request):
    return render(request, 'sol/reclamo.html', {})

def empleo(request):
    return render(request, 'sol/empleo.html', {})

def otro(request):
    return render(request, 'sol/otro.html', {})

def viajes(request):
    return render(request, 'sol/viajes.html', {})

def historia(request):
    return render(request, 'sol/historia.html', {})

def preguntas(request):
    Preguntas = Pregunta.objects.filter(respondida=True).order_by('-pk')

    paginator = Paginator(Preguntas, 10)

    page = request.GET.get('page')

    Preguntas = paginator.get_page(page)

    return render(request, 'sol/preguntas.html', {"Preguntas":Preguntas})

def resp_preguntas(request):
    if not request.user.is_superuser:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    Preguntas = Pregunta.objects.filter(respondida=False)
    return render(request, 'sol/resp_preguntas.html', {"Preguntas":Preguntas})

def pregunta_new(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            form = PreguntaForm(request.POST)
            if form.is_valid():
                Pregunta = form.save(commit=False)
                Pregunta.respuesta=""
                Pregunta.respondida = False
                Pregunta.save()
                messages.success(request,'¡Pregunta enviada exitosamente!')
                return redirect('preguntas')
        else:
            form = PreguntaLogueadoForm(request.POST)
            if form.is_valid():
                Pregunta = form.save(commit=False)
                Pregunta.nombre=request.user.username
                Pregunta.respuesta=""
                Pregunta.respondida = False
                Pregunta.save()
                messages.success(request,'¡Pregunta enviada exitosamente!')
                return redirect('preguntas')
    else:
        form = PreguntaForm()
    return render(request, 'sol/new_pregunta.html', {'form':form})

def pregunta_responder(request, pk):
    if not request.user.is_superuser:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
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

def pregunta_eliminar(request, pk):
    if not request.user.is_superuser:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    pregunta = get_object_or_404(Pregunta, pk=pk)
    pregunta.delete()
    messages.success(request,'¡Pregunta eliminada exitosamente!')
    return redirect('respPreguntas')

def mis_preguntas(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    Preguntas = Pregunta.objects.filter(nombre=request.user.username)
    return render(request, 'sol/mis_preguntas.html', {"Preguntas":Preguntas})

def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("preguntas")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "sol/registrarme.html",
                          context={"form":form})

    form = UserCreateForm
    return render(request = request,
                  template_name = "sol/registrarme.html",
                  context={"form":form})

#Ideas Concurso
def Ideas(request):
    Ideas = Idea.objects.filter(publicada=True).order_by('-pk')

    paginator = Paginator(Ideas, 10)

    page = request.GET.get('page')

    Ideas = paginator.get_page(page)

    return render(request, 'sol/idea/ideas.html', {"Preguntas":Ideas})

def nueva_idea(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            Idea = form.save(commit=False)
            Idea.publicada=False
            Idea.save()
            messages.success(request,'Idea enviada exitosamente!')
            return redirect('ideas')
    else:
        form = IdeaForm()
    return render(request, 'sol/idea/crear_idea.html', {'form':form})

def administrar_ideas(request):
    if not request.user.is_superuser:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    Ideas = Idea.objects.filter(publicada=False)
    return render(request, 'sol/idea/administrar_ideas.html', {"Ideas":Ideas})

def idea_eliminar(request, pk):
    if not request.user.is_superuser:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()
    messages.success(request,'¡Idea eliminada exitosamente!')
    return redirect('administrar_ideas')

def idea_aprobar(request, pk):
    if not request.user.is_superuser:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    idea = get_object_or_404(Idea, pk=pk)
    idea.publicada=True
    idea.save()
    messages.success(request,'¡Idea aprobada exitosamente!')
    return redirect('administrar_ideas')