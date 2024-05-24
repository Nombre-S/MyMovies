from django.db.models.fields import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from movies.models import Movie
from django.contrib import messages
from .forms import NameForm, MovieReviewForm
# Create your views here.

def movie_review(request, movie_id):
    if request.method == 'POST':
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            movie_id = form.cleaned_data['movie_id']
            rating = form.cleaned_data['rating']
            description = form.cleaned_data['description']
            movie = Movie.objects.get(pk=movie_id)
            user = request.user
            MovieReviewForm.objects.create(movie=movie, user=user, rating=rating, description=description)
            return redirect('movie_detail', movie_id)
    else:
        form = MovieReviewForm()
    return render(request, 'movies/review_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la vista index si las credenciales son válidas
            else:
                # Agrega un mensaje de error utilizando Django messages framework
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
                return redirect('login_view')
    else:
        return render(request, 'movies/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)
            # ...
            # redirect to a new URL:
            return render(request, "movies/name_ok.html", {"form": form})
        else:
            return render(request, "movies/name_ok.html", {"form": form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "movies/name.html", {"form": form})


def index(request):
    movies = Movie.objects.all()
    context = {'movie_list': movies}
    return render(request, "movies/index.html", context=context)

def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = {'movie': movie}
    return render(request, "movies/movie_detail.html", context=context)


