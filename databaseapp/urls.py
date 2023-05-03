from django.urls import path
from . import views
from django.urls import reverse
from django.contrib.auth import views as v

urlpatterns = [
    path('create', views.EmpresaCreateView.as_view(), name='empresa_create'),
    path('detail/<int:pk>', views.EmpresaDetailView.as_view(), name='empresa_detail'),
    path('update/<int:pk>', views.EmpresaUpdateView.as_view(), name='empresa_update'),
    path('delete/<int:pk>', views.EmpresaDeleteView.as_view(), name='empresa_delete'),
    path('', views.EmpresaListView.as_view(), name='empresa_list'),
    path('list', views.EmpresaList, name='empresa_list_filter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login-c'),
    # path('', views.index, name='index'),
]