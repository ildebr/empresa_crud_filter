from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Empresa
from .forms import NewEmpresaForm
from django.urls import reverse_lazy
from .filters import EmpresaFilter
from .forms import NewUserForm, UserLoginForm
from django.urls import reverse_lazy
from django.contrib import admin, messages
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [login_required(login_url="login-c")]

@method_decorator(decorators, name='dispatch')
class EmpresaCreateView(CreateView):
    model = Empresa
    # fields = '__all__'
    form_class = NewEmpresaForm
    success_url = reverse_lazy('empresa_list_filter')

@method_decorator(decorators, name='dispatch')
class EmpresaDetailView(DetailView):
    model =Empresa

    success_url = reverse_lazy('empresa_list_filter')

@method_decorator(decorators, name='dispatch')
class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = NewEmpresaForm
    success_url = reverse_lazy('empresa_list_filter')
    def get_context_data(self, **kwargs):
        context = super(EmpresaUpdateView, self).get_context_data(**kwargs)
        context['perra'] = 'perra'
        return context
    
    def dispatch(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk')
    
        return super(EmpresaUpdateView, self).dispatch(request, *args, **kwargs)

@method_decorator(decorators, name='dispatch')
class EmpresaDeleteView(DeleteView):
    model = Empresa
    success_url = reverse_lazy('empresa_list_filter')

@method_decorator(decorators, name='dispatch')
class EmpresaListView(ListView):
    model = Empresa

@login_required(login_url="login-c")
def EmpresaList(request):
    empresa_filter = EmpresaFilter(request.GET, queryset=Empresa.objects.all())
    context ={
        'form': empresa_filter.form,
        'empresas': empresa_filter.qs
    }

    return render(request, 'databaseapp/empresa_list_filter.html', context)

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        f = NewUserForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request,'account created')
            return HttpResponseRedirect(reverse('login'))
    else:
        f = NewUserForm()
    return render(request,'auth/register.html', {'form': f})


def login(request):
    if request.method == 'POST':
        f = UserLoginForm(request.POST)
        print(f)
        if f.is_valid():
            f.save()
            messages.success(request,'Login Successful')
            return HttpResponseRedirect(reverse('empresa_list_filter'))
        messages.error(request,'error')
    else:
        f = UserLoginForm()
    return render(request,'auth/login.html', {'form': f})