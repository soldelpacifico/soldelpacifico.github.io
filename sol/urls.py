from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tarifas', views.tarifas, name="tarifas"),
    path('pertenencias', views.pertenencias, name="pertenencias"),
    path('historia', views.historia, name="historia"),
    path('preguntas', views.preguntas, name="preguntas"),
    path('accounts/profile/', views.preguntas),
    path('preguntas/nueva', views.pregunta_new, name='pregunta_new'),
    path('preguntas/responder', views.resp_preguntas, name="respPreguntas"),
    path('preguntas/<int:pk>/', views.pregunta_responder, name='pregunta_responder'),
]