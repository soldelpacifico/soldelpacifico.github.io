from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index/', views.index),
    path('tarifas/', views.tarifas, name="tarifas"),
    path('pertenencias/', views.pertenencias, name="pertenencias"),
    path('nosotros/', views.nosotros, name="nosotros"),
]