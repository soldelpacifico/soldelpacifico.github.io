from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls import url
from rest_framework import routers
from sol.quickstart.views import AvisoViewSet, NoticiaViewSet, TarifaViewSet, InicioViewSet
from django.views.static import serve

router = routers.DefaultRouter()
router.register(r'avisos', AvisoViewSet)
router.register(r'noticias', NoticiaViewSet)
router.register(r'inicio', InicioViewSet)
router.register(r'tarifas', TarifaViewSet)

urlpatterns = [

    ##  API Urls
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    ##  App paths

    path('', views.index, name="index"),
    path('noticias', views.todasnoticias, name="noticias"),
    path('itinerarios', views.itinerarios, name="itinerarios"),
    path('rutas', views.rutas, name="rutas"),
    path('derechos', views.derechos, name="derechos"),
    path('tarifas', views.tarifas, name="tarifas"),
    path('beneficios', views.beneficios, name="beneficios"),
    path('pertenencias', views.pertenencias, name="pertenencias"),
    path('reclamo', views.reclamo, name="reclamo"),
    path('empleo', views.empleo, name="empleo"),
    path('otro', views.otro, name="otro"),
    path('viajes', views.viajes, name="viajes"),
    path('conocenos', views.historia, name="historia"),
    path('preguntas', views.preguntas, name="preguntas"),
    path('transrural', views.transrural, name='transrural'),
    path('terminales', views.terminales, name="terminales"),
    path('accounts/profile/', views.preguntas),
    path('preguntas/nueva', views.pregunta_new, name='pregunta_new'),
    path('preguntas/responder', views.resp_preguntas, name="respPreguntas"),
    path('preguntas/<int:pk>/', views.pregunta_responder, name='pregunta_responder'),
    path('preguntas/eliminar/<int:pk>/', views.pregunta_eliminar, name='pregunta_eliminar'),
    path('preguntas/propias', views.mis_preguntas, name='mis_preguntas'),
    path('ideas', views.Ideas, name="ideas"),
    path('ideas/crear', views.nueva_idea, name="nueva_idea"),
    path('ideas/administrar', views.administrar_ideas, name="administrar_ideas"),
    path('ideas/administrar/aprobar/<int:pk>/', views.idea_aprobar, name="aprobar_idea"),
    path('ideas/administrar/eliminar/<int:pk>/', views.idea_eliminar, name="eliminar_idea"),
    path('registrarme/', views.register, name='registrarme'),
    path('accounts/password-reset/', auth_views.PasswordResetView.as_view(template_name='sol/password_reset_form.html',email_template_name="sol/password_reset_email.html"), name="password_reset"),
    path('accounts/correo-enviado/', auth_views.PasswordResetDoneView.as_view(template_name='sol/password_reset_done.html'), name="password_reset_done"),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='sol/nueva_clave.html'), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='sol/clave_cambiada.html'), name='password_reset_complete'),
]