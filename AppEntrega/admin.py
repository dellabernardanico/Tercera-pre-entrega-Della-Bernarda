from django.contrib import admin
from.models import Clase, Instructor, Alumnos

class ClaseAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'repeticiones']
    search_fields = ['nombre', 'repeticiones']
    list_filter = ['nombre']

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'profesion']
    search_fields = ['nombre', 'apellido']
    list_filter = ['nombre']

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'certificado_medico']
    search_fields = ['nombre', 'apellido']
    list_filter = ['nombre']

    
# Register your models here.

admin.site.register(Clase, ClaseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Alumnos, AlumnoAdmin)