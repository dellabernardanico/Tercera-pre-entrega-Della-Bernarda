from django import forms


class ClaseFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    repeticiones = forms.IntegerField()

class InstructorFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField(required=False)
    profesion= forms.CharField(max_length=40, required=False)

class AlumnoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField(required=False)
    certificado_medico = forms.BooleanField(required=False, widget=forms.CheckboxInput)

class MiFormulario(forms.Form):
    repeticiones = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'number', 'step': '1'}),
        label='Repeticiones',
    )

from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']