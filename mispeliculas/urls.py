from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"), #si dejo el patho en blanco, le estoy diciendo que va a ser en la pàgina de inicio (cuando se visite el local host)
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('serie/', views.series, name="series"),
    path('capitulo/', views.capitulos, name="capitulos"),
    path('crearCapitulo/', views.crear_capitulo, name="crearCapitulo"),
    path('crearSerie/', views.crear_serie, name="crearSerie"),
    ]