from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# Create your models here.
class Persona(models.Model):
    nombre_text = models.CharField(max_length=200)
    apellido_text = models.CharField(max_length=200)
    fecha_nacimiento_date = models.DateTimeField('fecha de nacimiento')
    direccion_text = models.CharField(max_length=200)
    telefono_text = models.CharField(max_length=200,
                                     validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    dni_number = models.IntegerField(max_length=8)

    class Meta:
        abstract = True

class Medico(Persona):
    matricula_text = models.CharField(max_length=200)
    especialidad_text = models.CharField(max_length=200)


class Paciente(Persona):
    identificador_number = models.IntegerField(primary_key=True)
