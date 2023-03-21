from django.db import models

# Create your models here.

class Autores(models.Model):
    nombre = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    def __str__(self):
        return self.nombre
        
class Articulos(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField(max_length=10000)
    fecha = models.DateField()
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    articulo = models.ManyToManyField(Articulos)
    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    def __str__(self):
        return self.nombre