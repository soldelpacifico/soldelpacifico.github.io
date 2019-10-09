from django.shortcuts import render

def index(request):

    return render(request, 'sol/index.html', {})

def tarifas(request):

    return render(request, 'sol/tarifas.html', {})

def pertenencias(request):
    return render(request, 'sol/pertenencias.html', {})

def nosotros(request):
    return render(request, 'sol/nosotros.html', {})