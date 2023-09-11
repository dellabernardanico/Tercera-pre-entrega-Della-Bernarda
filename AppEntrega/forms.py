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
    certificado_medico = forms.BooleanField(required=False)