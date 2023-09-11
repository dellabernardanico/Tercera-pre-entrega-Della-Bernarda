from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import *
from .forms import *

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
            return render(req, "exito.html")
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
                return HttpResponse('Este instructor ya está registrado en el sistema.')
            
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
            return render(req, "exito.html")
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