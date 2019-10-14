from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tarifas', views.tarifas, name="tarifas"),
    path('pertenencias', views.pertenencias, name="pertenencias"),
    path('historia', views.historia, name="historia"),
]