from django.shortcuts import render
<<<<<<< HEAD

from django.utils import timezone


# Create your views here.

def index(request):
=======
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
>>>>>>> 4a019b9aef590ef3439be748c275eeaaafae660d
    return render(request, 'index.html', {})
