from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def inicio(request):
    return HttpResponse("Inicio")

def articulos(request):
    return HttpResponse("Articulos")

def autores(request):
    return HttpResponse("Autores")

def categorias(request):
    return HttpResponse("Categorias")

def contacto(request):
    return HttpResponse("Contacto")
