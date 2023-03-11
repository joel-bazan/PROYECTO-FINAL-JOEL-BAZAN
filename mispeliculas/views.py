from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Serie, Capitulo
from .forms import form_crearCapitulo, form_crearSerie
from django.contrib.auth.forms import UserCreationForm

def index(request):
    title= 'Django blog'
    return render(request,"index.html",{
        'title':title,
        'form':UserCreationForm
    })

def about(request):
    username='Joel'
    return render(request, "about.html", {
        'username':username
    })

# Create your views here.
def hello(request, username):


    return HttpResponse("<h2>Hello %s</h2>" % username)



def series(request):
    #series = list(Serie.objects.values())
    series = Serie.objects.values()
    return render (request, "series/serie.html",{
       'series':series 
    })

def capitulos(request):
    #capitulo = Capitulo.objects.get(nombre=nombre)
    capitulos = Capitulo.objects.all()
    return render (request, "capitulos/capitulo.html", {'capitulos':capitulos})

def crear_capitulo(request):
    if request.method == 'GET':  #(mostrar interfaz):
        return render (request, 'capitulos/crearCapitulo.html', {'form':form_crearCapitulo()})
   
    else:
        Capitulo.objects.create(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], serie_id=1)
        return redirect('capitulos')

def crear_serie(request):
    if request.method == 'GET':  #(mostrar interfaz):
        return render(request, 'series/crearSerie.html', {
        'form': form_crearSerie()
    })
    else:
        Serie.objects.create(titulo=request.POST["titulo"])
        return redirect('series')