from .models import Noticia

def probarCampos(self):
        noticia = Noticia()
        noticia.fecha_Publicacion = date.today
        noticia.titulo = 'Soy el titulo de una noticia'
        noticia.texto = 'Soy el texto que comunica la noticia.'
        return noticia