from django.contrib.auth.models import User
from django.db.models.fields import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import deactivate
from movies.models import Genre, Movie, MovieCredit, Person, MovieReview
from django.contrib import messages
from .forms import NameForm, MovieReviewForm
# Create your views here.

def movie_review(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            description = form.cleaned_data['review']
            user = request.user
            movieReview = MovieReview(user=user, movie=movie, rating=rating, review=description)
            movieReview.save()
            return redirect('movie_detail', movie_id )
        else:
            return render(request, 'movies/movie_detail.html', {'movie': movie, 'form': form})
    
    # Handle GET or other methods
    form = MovieReviewForm()
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'form': form})

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

def user_view(request, user_id):
    user = User.objects.get(pk=user_id)
    reviews = user.moviereview_set.all()
    context = {'reviews': reviews, 'user': user}
    return render(request, 'movies/user_detail.html', context)

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
    movie_list = [{
        'movie': movie,
        'average_rating': movie.get_average_rating()
    } for movie in movies]
    context = {'movie_list': movie_list}
    return render(request, "movies/index.html", context=context)


def discover_view(request):
    genre_id = request.GET.get('genre')
    if genre_id:
        movies = Movie.objects.filter(genres__id=genre_id).order_by('-release_date')
    else:
        movies = Movie.objects.all().order_by('-release_date')

    genres = Genre.objects.all()

    context = {
        'movie_list': movies,
        'genres': genres,
    }
    return render(request, 'movies/discover.html', context)



def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    credits = MovieCredit.objects.filter(movie_id=movie_id)
    reviews = MovieReview.objects.filter(movie_id=movie_id)
    average_rating = movie.get_average_rating()
    context = {
        'movie': movie,
        'credits': credits,
        'reviews': reviews,
        'average_rating': average_rating
    }
    return render(request, "movies/movie_detail.html", context=context)

def actor_detail(request, name):
    actor = Person.objects.filter(name=name).first()
    credits = MovieCredit.objects.filter(person_id=actor.id)
    context = {
        'person': actor,
        'credits': credits,
    }
    return render(request, "movies/actor_detail.html", context)
