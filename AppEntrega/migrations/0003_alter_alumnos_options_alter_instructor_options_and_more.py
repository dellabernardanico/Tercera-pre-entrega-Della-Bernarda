# Generated by Django 4.2.5 on 2023-09-11 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega', '0002_alter_clase_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnos',
            options={'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'verbose_name': 'Instructor', 'verbose_name_plural': 'Instructores'},
        ),
        migrations.AlterField(
            model_name='clase',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='alumnos',
            unique_together={('nombre', 'apellido')},
        ),
        migrations.AlterUniqueTogether(
            name='instructor',
            unique_together={('nombre', 'apellido')},
        ),
        migrations.RemoveField(
            model_name='alumnos',
            name='telefono',
        ),
    ]