from django.contrib import admin
from .models import Pelicula, Serie, Capitulo, Documentales
# Register your models here.

admin.site.register(Pelicula)
admin.site.register(Serie)
admin.site.register(Capitulo)
admin.site.register(Documentales)