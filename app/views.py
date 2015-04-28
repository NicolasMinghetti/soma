from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import logout
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html', {})

def graphe(request):
    return render(request, 'graphe.html', {})

def objectif(request):
    return render(request, 'objectif.html', {})

def reseaux(request):
    return render(request, 'reseaux.html', {})

def suggestions(request):
    return render(request, 'suggestions.html', {})

def test_view(request):
    return render(request, 'test_view.html', {})

def logout_view(request):
    logout(request)
    return render(request, 'index.html', {})
