
from django.urls import path
from tragedia.views import *

urlpatterns = [
    path('index', index, name='index'),
    path('', inicio, name='inicio'),
    path('articulos/', articulos, name='articulos'),
    path('autores/', autores, name='autores'),
    path('categorias/', categorias, name='categorias'),
    path('contacto/', contacto, name='contacto'),
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
]
   