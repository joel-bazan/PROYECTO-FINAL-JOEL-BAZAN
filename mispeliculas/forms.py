from django import forms

class form_crearCapitulo(forms.Form):
    nombre = forms.CharField(label="Nombre del capítulo", max_length=200)
    descripcion = forms.CharField(label= "Descripción",widget=forms.Textarea)

class form_crearSerie(forms.Form):
    titulo=forms.CharField(label="Titulo de la serie", max_length=200)
    """
    genero = forms.CharField(max_length=200)
    fecha = forms.DateField
    temporadas= forms.IntegerField(default=1)
    completada=forms.BooleanField(default=False)
    descargada=forms.BooleanField(default=False)
    """
