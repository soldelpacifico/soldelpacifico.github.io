from django.test import TestCase
from sol.models import Noticia, Aviso
from datetime import datetime

class testModelo(TestCase):
    def test_noticia(self):
        noticia1 = Noticia(titulo='TituloNoticia', texto='blabla')
        noticia1.save()

        noticiadb= Noticia.objects.get(pk=1)
        self.assertEqual(noticiadb.titulo,noticia1.titulo)
        self.assertEqual(noticiadb.texto,'blabla')
        self.assertEqual(noticiadb.fecha_Publicacion,None)
    
    def test_aviso_publicar(self):
        aviso1 = Aviso(dia="11/02/2029",titulo='Aviso del futuro', mensaje='Comunico desde el futuro')
        assert aviso1.dia == "11/02/2029"
        self.assertEquals(aviso1.__str__(),'Comunico desde el futuro')

        
