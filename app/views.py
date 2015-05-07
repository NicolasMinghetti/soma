from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import logout
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html', {})

def graphe(request):
    return render(request, 'graphe.html', {})

def objectif(request):
    current_path=get_current_path(request)
    return render(request, 'objectif.html', {'current_path':current_path})

def objectifChoisir(request):
    current_path=get_current_path(request)
    return render(request, 'objectifChoisir.html', {'current_path':current_path})


def reseaux(request):
    return render(request, 'reseaux.html', {})

def suggestions(request):
    return render(request, 'suggestions.html', {})

def test_view(request):
    return render(request, 'test_view.html', {})

def logout_view(request):
    logout(request)
    return render(request, 'index.html', {})


def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }
