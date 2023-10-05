from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('clase-formulario/', claseFormulario, name="ClaseFormulario"),
    path('instructor-formulario/', instructorFormulario, name="InstructorFormulario"),
    path('alumno-formulario/', alumnoFormulario, name="AlumnoFormulario"),
    path('busqueda-clase/', busquedaClase, name="BusquedaClase"),
    path('buscar/', buscar, name="Buscar"),
    path('', inicio, name="Inicio"),
    path('listaInstructores/', lista_instructores, name="ListaInstructores"),
    path('listaClases/', lista_clases, name="ListaClases"),
    path('eliminarClases/<pk>/', ClaseDelete.as_view(), name="EliminarClases"),
    # path('creaInstructor/', crea_instructor, name="CreaInstructores"),
    path('eliminarInstructor/<pk>/', InstructorDelete.as_view(), name="EliminarInstructores"),
    path('editarInstructor/<int:id>', editar_instructor, name="EditarInstructor"),
    path('listaAlumnos/', lista_alumnos, name="ListaAlumnos"),
    # path('creaAlumnos/', crea_alumnos, name="CreaAlumnos"),
    path('eliminarAlumnos/<pk>/', AlumnosDelete.as_view(), name="EliminarAlumnos"),
    path('editarAlumnos/<int:id>', editar_alumnos, name="EditarAlumnos"),
    path('editarClase/<int:id>', editar_clase, name="EditarClase"),
    # path('login/', views.login_request, name="Login"),
    path('login/', loginView, name="Login"),
    path('register/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('comentarios/<int:publicacion_id>/', ver_y_agregar_comentario, name="ver_y_agregar_comentario"),
    path('ver_comentarios/', ver_comentarios, name='ver_comentarios'),
    path('agregar_comentario/', agregar_comentario, name='agregar_comentario'),
    path('editar_comentario/<int:comentario_id>/', editar_comentario, name='editar_comentario'),
    path('eliminar_comentario/<int:comentario_id>/', eliminar_comentario, name='eliminar_comentario'),
    path('acerca-nosotros/', acerca_nosotros , name='acerca_nosotros'),

]