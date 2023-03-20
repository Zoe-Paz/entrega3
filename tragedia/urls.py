"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.urls import path
from tragedia import views

urlpatterns = [
    path("", views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),
    path('articulos/', views.articulos, name="articulos"),
    path('autores/', views.autores, name="autores"),
    path('categorias/', views.categorias, name="categorias"),
    path('contacto/', views.contacto, name="contacto"),
]
