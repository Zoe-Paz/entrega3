from django.db import models

# Create your models here.

class autor(models.Model):
    nombre = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    def __str__(self):
        return self.nombre

class articulo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField(max_length=10000)
    fecha = models.DateField()
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class categoria(models.Model):
    nombre = models.CharField(max_length=50)
    articulo = models.ManyToManyField(articulo)
    def __str__(self):
        return self.nombre