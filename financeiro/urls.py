from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_honorarios, name='lista_honorarios'),
    path('novo/', views.novo_honorario, name='novo_honorario'),
    path('editar/<int:id>/', views.editar_honorario, name='editar_honorario'),
]