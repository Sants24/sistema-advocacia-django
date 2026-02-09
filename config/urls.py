from django.contrib import admin
from django.urls import path, include
from core.views import home, cadastro  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/cadastro/', cadastro, name='cadastro'),
    path('clientes/', include('core.urls')),
    path('financeiro/', include('financeiro.urls')),
]