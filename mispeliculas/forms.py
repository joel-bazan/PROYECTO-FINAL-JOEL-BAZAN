from django import forms
from django.forms import ModelForm
from .models import Capitulo, Serie, Pelicula




class form_crearCapitulo(ModelForm):
 class Meta:
        model=Capitulo
        fields=['numero','nombre','descripcion','temporada','serie','visto','fecha_emision','reseña']
    #nombre = forms.CharField(label="Nombre del capítulo", max_length=200)
    #descripcion = forms.CharField(label= "Descripción",widget=forms.Textarea)

class form_crearSerie(ModelForm):
    class Meta:
        model=Serie
        fields=['titulo','genero','fecha','temporadas','completada','descargada','reseña']

"""
    titulo=forms.CharField(label="Titulo de la serie", max_length=200)
    genero = forms.CharField(max_length=200)
    fecha = forms.DateField
    temporadas= forms.IntegerField()
    completada=forms.BooleanField()
    descargada=forms.BooleanField()
    """

class form_crearPelicula(ModelForm):
    class Meta:
        model=Pelicula
        fields=['titulo','genero','fecha','descargada','reseña']

    #titulo=forms.CharField(label="Titulo de la pelicula", max_length=200)
