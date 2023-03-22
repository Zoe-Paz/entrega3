"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.urls import path
from tragedia import views

urlpatterns = [
    path('index/', views.index, name="Index"),
    path('', views.inicio, name="Inicio"),
    path('articulos/', views.articulos, name="Articulos"),
    path('autores/', views.autores, name="Autores"),
    path('categorias/', views.categorias, name="Categorias"),
    path('contacto/', views.contacto, name="Contacto"),
    path('cursoFormulario', views.cursoFormulario, name= "CursoFormulario"),
]
