from django import forms

from .models import Pregunta

class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta
        fields = ('nombre', 'email','pregunta',)

class RespuestaForm(forms.ModelForm):

    class Meta:
        model = Pregunta
        fields = ('respuesta',)