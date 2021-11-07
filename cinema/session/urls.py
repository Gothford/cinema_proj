from django.urls import path
from .views import *

urlpatterns = [
    path('films', GetAllFilms.as_view()),
]