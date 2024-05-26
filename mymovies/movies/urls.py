from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/discover/", views.discover_view, name="discover_view"),
    path("movies/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("movies/<int:movie_id>/review/submit/", views.movie_review, name="movie_review"),
    path("<str:name>", views.actor_detail, name="actor_detail"),
    path("movies/your_name/", views.get_name, name="get_name"),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('user/<int:user_id>', views.user_view, name='user_view'),
]
