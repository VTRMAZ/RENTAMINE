from django.urls import path
from django.shortcuts import render
from . import views


def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', views.home, name='home'),
]
