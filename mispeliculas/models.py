from django.db import models

# Create your models here.
class Pelicula (models.Model):
    titulo=models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    director=models.CharField(max_length=200, blank=True)
    fecha = models.DateField
    descargada=models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.titulo

class Serie (models.Model):
    titulo=models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    fecha = models.DateField
    temporadas= models.IntegerField(default=1)
    completada=models.BooleanField(default=False)
    descargada=models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Capitulo (models.Model):
    numero= models.IntegerField(default=0)
    temporada= models.IntegerField(default=0)
    serie=models.ForeignKey(Serie, on_delete=models.CASCADE)
    fecha_emision=models.DateField

    def __str__(self):
        return self.serie.titulo +"" + self.temporada + "x" + self.numero

class Documentales (models.Model):
    numero= models.IntegerField(default=0)
    temporada= models.IntegerField(default=0)
    serie=models.ForeignKey(Serie, on_delete=models.CASCADE)
    fecha_emision=models.DateField

    def __str__(self):
        return self.serie.titulo
    
""""
    pelicula=Pelicula(titulo='Rocky', director= 'Sylvester Stallone')
    pelicula.save()
    lista_peliculas = Pelicula.objects.aall()
    print(lista_pelicula)

    pelicula= Pelicula.objects.get(titulo='Rocky')
    print(pelicula.titulo)

    pelicula= Pelicula.objects.get(titulo='Rocky')
    pelicula.delete

    pelicula= Pelicula.objects.get(titulo='Rocky')
    pelicula.director='otro'
    pelicula.save()
"""