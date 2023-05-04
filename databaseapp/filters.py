import django_filters

from .models import Empresa

class EmpresaFilter(django_filters.FilterSet):
    class Meta:
        model = Empresa
        fields = ['nombre_empresa', 
                'direccion', 
                'CP', 
                'localidad', 
                'sub_localidad', 
                'comunidad_autonoma', 
                'telefono', 
                'telefono_adicional', 
                'email', 
                'sitio_web', 
                'actividad', 
                'forma_social', 
                'sub_sector', 
                'facturacion', 
                'nro_empleados', 
                'capital', 
                'facebook', 
                'instagram', 
                'twitter', 
                'youtube', 
                'booksy',
                'tiene_booksy', 
                'estado' ]
        