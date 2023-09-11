from django.urls import path
from .views import *

urlpatterns = [
    path('clase-formulario/', claseFormulario, name="ClaseFormulario"),
    path('instructor-formulario/', instructorFormulario, name="InstructorFormulario"),
    path('alumno-formulario/', alumnoFormulario, name="AlumnoFormulario"),
    path('busqueda-clase/', busquedaClase, name="BusquedaClase"),
    path('buscar/', buscar, name="Buscar"),
    path('', inicio, name="Inicio")
]