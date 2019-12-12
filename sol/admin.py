from django.contrib import admin
from .models import Noticia, Pregunta, Aviso, Inicio, Tarifa, NoticiaTrans

admin.site.register(Noticia)
admin.site.register(Pregunta)
admin.site.register(Aviso)
admin.site.register(Inicio)
admin.site.register(Tarifa)
admin.site.register(NoticiaTrans)