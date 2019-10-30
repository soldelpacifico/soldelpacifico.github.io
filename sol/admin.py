from django.contrib import admin
from .models import Noticia, Pregunta, Aviso

admin.site.register(Noticia)
admin.site.register(Pregunta)
admin.site.register(Aviso)