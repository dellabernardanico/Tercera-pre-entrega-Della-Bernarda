from django.db import models

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    repeticiones = models.IntegerField()

    class Meta():

        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'
        unique_together = ('nombre', 'repeticiones')
    

class Instructor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    clases = models.ManyToManyField(Clase)

    class Meta():

        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'
        unique_together = ('nombre', 'apellido')

class Alumnos(models.Model):

    nombre = models.CharField(max_length= 40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    certificado_medico = models.BooleanField(default=False)

    class Meta():

        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        unique_together = ('nombre', 'apellido')
