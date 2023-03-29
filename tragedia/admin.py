from django.contrib import admin
from .models import Autor, Categoria, Comprador


# Register your models here.
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Comprador)