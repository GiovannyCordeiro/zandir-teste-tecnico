from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_movies, name='get_all_movies') 
]
