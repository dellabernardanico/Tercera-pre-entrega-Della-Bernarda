from django.http import HttpResponse, HttpRequest,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from .models import *
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(req):

    return render(req, "inicio.html")

def claseFormulario(req):
    
    if req.method == 'POST':
        miFormulario = ClaseFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nombre = data["nombre"]
            repeticiones = data["repeticiones"]
            
            if Clase.objects.filter(nombre=nombre, repeticiones=repeticiones).exists():
                return HttpResponse('Ya existe una clase con ese nombre y repeticiones semanales.')
            
            clase = Clase(nombre=nombre, repeticiones=repeticiones)
            clase.save()
            return render(req, "inicio.html")
    else:
        miFormulario = ClaseFormulario()
        return render(req, "claseFormulario.html", {"miFormulario": miFormulario})
    
    

    
def instructorFormulario(req):
    
    if req.method == 'POST':
        miFormulario = InstructorFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            
            if Instructor.objects.filter(nombre=nombre, apellido=apellido).exists():
                # Redirige al usuario nuevamente al formulario si ya existe un instructor
                return HttpResponseRedirect(reverse('InstructorFormulario'))
            
            instructor = Instructor(nombre=nombre, apellido=apellido)
            instructor.save()
            return render(req, "inicio.html")
    else:
        miFormulario = InstructorFormulario()
        return render(req, "instructorFormulario.html", {"miFormulario": miFormulario})

def alumnoFormulario(req):
    
    if req.method == 'POST':
        miFormulario = AlumnoFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            
            if Alumnos.objects.filter(nombre=nombre, apellido=apellido).exists():
                return HttpResponse('Este alumno ya está registrado en el sistema.')
            
            alumno = Alumnos(nombre=nombre, apellido=apellido, certificado_medico=True)
            alumno.save()
            return render(req, "inicio.html")
    else:
        miFormulario = AlumnoFormulario()
        return render(req, "alumnoFormulario.html", {"miFormulario": miFormulario})


    
def busquedaClase(req):
   
    return render(req, "inicio.html")

def buscar(req: HttpRequest):
    if req.GET.get("nombre"):
        nombre = req.GET["nombre"]
        try:
            clases = Clase.objects.filter(nombre__icontains=nombre)
            if clases:
                return render(req, "resultadosBusqueda.html", {"clases": clases})
            else:
                return HttpResponse('No se encontraron clases con el nombre especificado.')
        except Clase.DoesNotExist:
            return HttpResponse('La clase todavía no está disponible. Próximamente agregaremos esta clase al catálogo.')
    else:
        return HttpResponse('Debe agregar el nombre de una clase.')
    
# @staff_member_required(login_url='/app-coder/login')
def lista_instructores(req):

    instructores = Instructor.objects.all()

    return render(req, "listaInstructores.html", {"instructores": instructores})

# def crea_instructor(req):
#     if req.method == 'POST':
#         miFormulario = InstructorFormulario(req.POST)

#         if miFormulario.is_valid():
#             data = miFormulario.cleaned_data

#             try:
#                 # Intentar crear el instructor
#                 instructor = Instructor(
#                     nombre=data["nombre"],
#                     apellido=data["apellido"],
#                     email=data["email"],
#                     profesion=data["profesion"]
#                 )
#                 instructor.save()

#                 return render(req, "inicio.html")

#             except IntegrityError:
#                 # Mostrar el mensaje de error cambiando su estilo CSS
#                 error_message = "Ya existe un instructor con este nombre y apellido."
#                 miFormulario.add_error(None, error_message)
#                 return render(req, "instructorFormulario.html", {"miFormulario": miFormulario})

#     else:
#         miFormulario = InstructorFormulario()

#     return render(req, "instructorFormulario.html", {"miFormulario": miFormulario})
    
class InstructorDelete(LoginRequiredMixin, DeleteView):
    model = Instructor
    template_name = "eliminarInstructor.html"
    success_url = '/listaInstructores'
    context_object_name = "instructor"


@login_required(login_url='/login')
def editar_instructor(req, id):

    instructor = Instructor.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = InstructorFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            instructor.nombre = data["nombre"]
            instructor.apellido = data["apellido"]
            instructor.email = data["email"]
            instructor.profesion = data["profesion"]
            instructor.save()

            return render(req, "inicio.html")
    else:

        miFormulario = InstructorFormulario(initial={
            "nombre": instructor.nombre,
            "apellido": instructor.apellido,
            "email": instructor.email,
            "profesion": instructor.profesion,
        })
        return render(req, "editarInstructor.html", {"miFormulario": miFormulario, "id": instructor.id})
    
###ahora van los alumnos:
def lista_alumnos(req):

    alumnos = Alumnos.objects.all()

    return render(req, "listaAlumnos.html", {"alumnos": alumnos})

# def crea_alumnos(req):

#     if req.method == 'POST':

#         miFormulario = AlumnoFormulario(req.POST)

#         if miFormulario.is_valid():

#             data = miFormulario.cleaned_data
#             alumnos = Instructor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], certificado=data["certificado"])
#             alumnos.save() 

#             return render(req, "inicio.html")
#     else:

#         miFormulario = AlumnoFormulario()
#         return render(req, "alumnosFormulario.html", {"miFormulario": miFormulario})
    
class AlumnosDelete(LoginRequiredMixin, DeleteView):
    model = Alumnos
    template_name = "eliminarAlumnos.html"
    success_url = '/listaAlumnos'
    context_object_name = "alumnos"


@login_required(login_url='/login')
def editar_alumnos(req, id):

    alumnos = Alumnos.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = AlumnoFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            alumnos.nombre = data["nombre"]
            alumnos.apellido = data["apellido"]
            alumnos.email = data["email"]
            alumnos.certificado_medico = data["certificado_medico"]
            alumnos.save()

            return render(req, "inicio.html")
    else:

        miFormulario = AlumnoFormulario(initial={
            "nombre": alumnos.nombre,
            "apellido": alumnos.apellido,
            "email": alumnos.email,
            "certificado": alumnos.certificado_medico,
        })
        return render(req, "editarAlumnos.html", {"miFormulario": miFormulario, "id": alumnos.id})
    
def lista_clases(req):

    clases = Clase.objects.all()

    return render(req, "listaClases.html", {"clases": clases})

class ClaseDelete(LoginRequiredMixin, DeleteView):
    model = Clase
    template_name = "eliminarClases.html"
    success_url = '/listaClases'
    context_object_name = "clase"


@login_required(login_url='/login')
def editar_clase(req, id):

    clase = Clase.objects.get(id=id)

    if req.method == 'POST':
        
        miFormulario = ClaseFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            clase.nombre = data["nombre"]
            clase.repeticiones = data["repeticiones"]
            clase.save()

            return render(req, "inicio.html")
    else:
        
        miFormulario = ClaseFormulario(initial={
            "nombre": clase.nombre,
            "repeticiones": clase.repeticiones,
        })

    return render(req, 'editarClase.html', {'miFormulario': miFormulario, 'id': clase.id})

def loginView(req):

    if req.method == 'POST':
        
        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username = usuario, password = psw)
            
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}!"})

        return render(req, "inicio.html", {"mensaje": f"Datos incorrectos!"})
    else:
        
        miFormulario = AuthenticationForm()
        return render(req, 'login.html', {'miFormulario': miFormulario})
    
def register(req):

    if req.method == 'POST':
        
        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con exito!"})

        return render(req, "inicio.html", {"mensaje": f"Formulario incorrectos!"})
    else:
        
        miFormulario = UserCreationForm()
        return render(req, 'registro.html', {'miFormulario': miFormulario})
    

def ver_comentarios(req):
    comentarios = Comentario.objects.all()
    return render(req, 'ver_comentarios.html', {'comentarios': comentarios})


@login_required(login_url='/login')
def agregar_comentario(req):
    if req.method == 'POST':
        miFormulario = ComentarioForm(req.POST)
        if miFormulario.is_valid():
            comentario = miFormulario.save(commit=False)
            comentario.autor = req.user  # Asocia el autor al usuario actual
            comentario.save()
            # Puedes redirigir a la página de comentarios o a donde prefieras
            return redirect('ver_comentarios')

    else:
        miFormulario = ComentarioForm()
    return render(req, 'agregar_comentario.html', {'miFormulario': miFormulario})
    
@login_required
def ver_y_agregar_comentario(req, publicacion_id):
    publicacion = Publicacion.objects.get(id=publicacion_id)

    if req.method == 'POST':
        miFormulario = ComentarioForm(req.POST)
        if miFormulario.is_valid():
            comentario = miFormulario.save(commit=False)
            comentario.autor = req.user
            comentario.publicacion = publicacion
            comentario.save()
            miFormulario = ComentarioForm()  # Limpiar el formulario después de enviar un comentario válido

    else:
        miFormulario = ComentarioForm()

    comentarios = Comentario.objects.filter(publicacion=publicacion)

    return render(req, 'ver_y_agregar_comentario.html', {'publicacion': publicacion, 'comentarios': comentarios, 'miFormulario': miFormulario})


@login_required(login_url='/login')
def editar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            # Después de editar el comentario, redirigir a la página de comentarios.
            return redirect('ver_comentarios')

    else:
        form = ComentarioForm(instance=comentario)

    return render(request, 'editar_comentario.html', {'form': form, 'comentario': comentario})



@login_required(login_url='/login')
def eliminar_comentario(req, comentario_id):
    comentario = Comentario.objects.get(pk=comentario_id)
    comentario.delete()
    return redirect('ver_comentarios')

def acerca_nosotros(request):
    return render(request, 'acerca.html')