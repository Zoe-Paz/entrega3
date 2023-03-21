from django import forms

class AutoresFormulario(forms.Form):
    autores= forms.CharField()
    articulos = forms.IntegerField()
    categorias = forms.CharField()
    