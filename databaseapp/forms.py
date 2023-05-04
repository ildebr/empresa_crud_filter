from django import forms
from .models import Empresa
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

class NewEmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = '__all__'
        exclude = ('pk',)
    def __init__(self, *args, **kwargs):
        super(NewEmpresaForm, self).__init__(*args, **kwargs)
        self.fields['nombre_empresa'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['direccion'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['CP'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['localidad'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['sub_localidad'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['comunidad_autonoma'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['telefono'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['telefono_adicional'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['email'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['sitio_web'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['actividad'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['forma_social'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['sub_sector'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['facturacion'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['nro_empleados'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['capital'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['facebook'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['instagram'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['twitter'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['youtube'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['booksy'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['estado'].widget.attrs.update({'class':'input_field form-control'})
        self.fields['nota'].widget.attrs.update({'class':'input_field form-control'})


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input_field form-control', 'required': 'required'})
        self.fields['username'].widget.attrs.update({'class': 'input_field form-control', 'required': 'required'})
        self.fields['password1'].widget.attrs.update({'class': 'input_field form-control', 'required': 'required'})
        self.fields['password2'].widget.attrs.update({'class': 'input_field form-control', 'required': 'required'})

    class Meta:
        model = User
        fields = ("username", "email")
    
    def save(self,commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'user input_field form-control', 'id': 'user', 'required': 'required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password input_field'}))
