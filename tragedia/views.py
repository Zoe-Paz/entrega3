from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "tragedia/padre.html")

def inicio(request):
     return render(request, 'tragedia/inicio.html', {})

def articulos(request):
    return render(request, 'tragedia/articulos.html', {})

def autores(request):
    return render(request, 'tragedia/autores.html', {})

def categorias(request):
    return render(request, 'tragedia/categorias.html', {})

def contacto(request):
    return render(request, 'tragedia/contacto.html', {})

def cursoFormulario(request):

    return render(request, 'tragedia/cursoFormulario.html')
