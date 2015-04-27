from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

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

def logout_view(request):
    logout(request)
    return render(request, 'index.html', {})


def test_view(request):
    if request.user.is_authenticated():
        u = request.user
        username = u.username
        user_facebook_link = u.userprofile.facebook_link
        # user_facebook_link = u.UserProfile.facebook_link
        return render(request, 'test_view.html', {'username':username, 'user_facebook_link':user_facebook_link})
    else :
        return render(request, 'test_view.html')
