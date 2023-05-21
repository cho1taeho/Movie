from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.home),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('random/', views.random),
    path('themes/', views.themes),
    path('recommend/', views.recommend),
]
