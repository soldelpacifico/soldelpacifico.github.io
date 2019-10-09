from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

def index(request):
    tmp=get_template('index.html')
    document=tmp.render()
    return HttpResponse(document)

def tarifas(request):
    tmp=get_template('tarifas.html')
    document=tmp.render()
    return HttpResponse(document)

def pertenencias(request):
    tmp=get_template('pertenencias.html')
    document=tmp.render()
    return HttpResponse(document)

def nosotros(request):
    tmp=get_template('nosotros.html')
    document=tmp.render()
    return HttpResponse(document)