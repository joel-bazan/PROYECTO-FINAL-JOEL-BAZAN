from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Serie, Capitulo
from .forms import form_crearCapitulo, form_crearSerie, form_crearPelicula
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def index(request):
    title = 'Reseñas de películas'
    return render(request, "index.html", {
        'title': title,
    })


def signup(request):
    if request.method == 'GET':  # (mostrar interfaz):
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def signout(request):
    logout(request)
    return redirect('index')


def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrectos'
        })
        else:
            login(request, user)
            return redirect('index')


def about(request):
    username = 'Joel'
    return render(request, "about.html", {
        'username': username
    })

# Create your views here.


def hello(request, username):

    return HttpResponse("<h2>Hello %s</h2>" % username)


def series(request):
    # series = list(Serie.objects.values())
    series = Serie.objects.values()
    return render(request, "series/serie.html", {
        'series': series
    })


def capitulos(request):
    # capitulo = Capitulo.objects.get(nombre=nombre)
    capitulos = Capitulo.objects.all()
    return render(request, "capitulos/capitulo.html", {'capitulos': capitulos})


def crear_capitulo(request):
    if request.method == 'GET':  # (mostrar interfaz):
        return render(request, 'capitulos/crearCapitulo.html', {'form': form_crearCapitulo()})

    else:
        Capitulo.objects.create(
            nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], serie_id=1)
        return redirect('capitulos')


def crear_serie(request):
    if request.method == 'GET':  # (mostrar interfaz):
        return render(request, 'series/crearSerie.html', {
            'form': form_crearSerie()
        })
    else:
        Serie.objects.create(titulo=request.POST["titulo"])
        return redirect('series')


def crear_pelicula(request):
    if request.method == 'GET':  # (mostrar interfaz):
        return render(request, 'peliculas/crearPelicula.html', {
            'form': form_crearPelicula()
        })
    else:
        Serie.objects.create(titulo=request.POST["titulo"])
        return redirect('peliculas')
