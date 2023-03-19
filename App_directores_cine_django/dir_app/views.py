from django.shortcuts import render
from .models import Director, Movie, Genre
# Create your views here.
def index(request):
    return render(
        request,
        'index.html'
    )

def directores(request):

    directores_list = Director.objects.all()
    context = {
        "directores_list": directores_list
    }
    return render(
        request,
        "directores.html",
        context=context
    )

def dir_details(request, id):
    director = Director.objects.get(id=id)
    peliculas_de_director = Movie.objects.filter(director=director).values()
    context = {
        "director": director,
        "peliculas_de_director": peliculas_de_director,
    }
    return render(
        request,
        "dir_details.html",
        context=context
    )