from django.db import models
from django.urls import reverse

# Create your models here.

class Empresa(models.Model):

    OPTIONS = (
        ('C', 'COOL'),
        ('W', 'WARM'),
    )
    FACTURACION_OPCIONES = (
        (0,'0€ - 500.000€'),
        (1, '500.000€ - 1.000.000€'),
        (2, '1.000.000€ - 2.500.000€'),
        (3, 'mayor a 2.500.000€'),
    )

    EMPLEADO_OPCIONES = (
        (0,'0-10'),
        (1, '10-50'),
        (2, '50-200'),
        (3, '200+'),
    )

    CAPITAL_OPCIONES = (
        (0,'0€ - 3.500€'),
        (1, '3.500€ - 10.000€'),
        (2, '10.000€ - 50.000€'),
        (3, '50.000€ - 100.000€'),
        (4, 'mayor a 100.000€'),
    )

    ESTADO_OPCIONES = (
        ('R','RECHAZADO'),
        ('P', 'PENDIENTE'),
        ('I', 'NEGOCIACIONES'),
        ('A', 'ACEPTADO'),
    )
    nombre_empresa = models.CharField(max_length=300,blank=True, null= True, unique= True)
    direccion = models.CharField(max_length=300,blank=True, null= True)
    CP = models.IntegerField()
    localidad = models.CharField(max_length=100,blank=True, null= True)
    sub_localidad = models.CharField(max_length=100,blank=True, null= True)
    comunidad_autonoma = models.CharField(max_length=300,blank=True, null= True)
    telefono = models.CharField(max_length=100,blank=True, null= True, unique= True)
    telefono_adicional = models.CharField(max_length=100, blank=True, null= True, unique= True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    sitio_web = models.CharField(max_length=300,blank=True, null= True)
    actividad = models.CharField(max_length=300,blank=True, null= True)
    forma_social = models.CharField(max_length=300, blank=True, null=True)
    sub_sector = models.CharField(max_length=300,blank=True, null= True, unique= True)
    facturacion = models.CharField(max_length=60, choices=FACTURACION_OPCIONES, blank=True, null=True)
    nro_empleados = models.CharField(max_length=60, choices=EMPLEADO_OPCIONES, blank=True, null=True)
    capital = models.CharField(max_length=60, choices=CAPITAL_OPCIONES, blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null= True)
    instagram = models.CharField(max_length=300, blank=True, null= True)
    twitter = models.CharField(max_length=300, blank=True, null= True)
    youtube = models.CharField(max_length=300, blank=True, null= True)
    booksy = models.CharField(max_length=20, blank=True, null= True)
    estado = models.CharField(choices=ESTADO_OPCIONES, max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_empresa}"
    
    def get_absolute_url(self):
        return reverse('empresa_update', args=[str(self.id)])
