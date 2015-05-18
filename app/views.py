from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import NameForm
from .models import UserProfile

from django.http import HttpResponseRedirect

def index(request):
    if request.user :
        print("is authenticated :) ")
        return render(request, 'index.html')
    else:
        print("not authenticated")
        return render(request, 'index.html')



#
# def index(request):
#     return render(request, 'index.html', {})

def graphe(request):
    return render(request, 'graphe.html', {})

#def objectif(request):
#    current_path=get_current_path(request)
#    if request.user.is_authenticated():
#        print("bite")
#    return render(request, 'objectif.html', {'current_path':current_path})
#
def objectifChoisir(request):
    current_path=get_current_path(request)
    return render(request, 'objectifChoisir.html', {'current_path':current_path})

def name(request):
    current_path=get_current_path(request)
    return render(request, 'name.html', {'current_path':current_path})

def objectif(request):
    current_path=get_current_path(request)
    profile=UserProfile.objects.get(user=request.user)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            profile.objectif.append("new")
            print(request.POST['choix'])
            print(profile.objectif)
            if profile.objectif1=="Null":
                profile.objectif1=request.POST['choix']
                profile.objectif1a=request.POST['choix1']
                profile.objectif1b=request.POST['choix2']
                profile.objectif1c=request.POST['choix3']
            elif profile.objectif2=="Null":
                profile.objectif2=request.POST['choix']
                profile.objectif2a=request.POST['choix1']
                profile.objectif2b=request.POST['choix2']
                profile.objectif2c=request.POST['choix3']
            else:
                profile.objectif3=request.POST['choix']
                profile.objectif3a=request.POST['choix1']
                profile.objectif3b=request.POST['choix2']
                profile.objectif3c=request.POST['choix3']
            profile.save()
            print("On sauvegarde...")
            # redirect to a new URL:
            print("Debut ojectif")
            print(profile.objectif1)
            print(profile.objectif2)
            print(profile.objectif3)
            print("/fin objectif")


            return HttpResponseRedirect('/VosObjectifs/')
        else:
            return render(request, 'erreur.html', {'message':'Tu n\'as pas rempli le formulair corectement !'})

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'objectif.html', {'current_path':current_path})

def recherche(request):
    current_path=get_current_path(request)
    return render(request, 'recherche.html', {'current_path':current_path})

def vosObjectifs(request):
    current_path=get_current_path(request)
    profile=UserProfile.objects.get(user=request.user)
    return render(request, 'VosObjectifs.html', {'current_path':current_path,'objectif1':profile.objectif1,'objectif1a':profile.objectif1a,'objectif1b':profile.objectif1b,'objectif1c':profile.objectif1c,'objectif2':profile.objectif2,'objectif2a':profile.objectif2a,'objectif2b':profile.objectif2b,'objectif2c':profile.objectif2c,'objectif3':profile.objectif3,'objectif3a':profile.objectif3a, 'objectif3b':profile.objectif3b, 'objectif3c':profile.objectif3c})

def vosObjectifsSupprimer1(request):
    current_path=get_current_path(request)
    profile=UserProfile.objects.get(user=request.user)

    profile.objectif1="Null"
    profile.objectif1a="Vous n'avez pas défini d'objectif"
    profile.objectif1b=""
    profile.objectif1c=""
    profile.save()
    return HttpResponseRedirect('/VosObjectifs/')

def vosObjectifsSupprimer2(request):
    current_path=get_current_path(request)
    profile=UserProfile.objects.get(user=request.user)

    profile.objectif2="Null"
    profile.objectif2a="Vous n'avez pas défini d'objectif"
    profile.objectif2b=""
    profile.objectif2c=""
    profile.save()
    return HttpResponseRedirect('/VosObjectifs/')

def vosObjectifsSupprimer3(request):
    current_path=get_current_path(request)
    profile=UserProfile.objects.get(user=request.user)

    profile.objectif3="Null"
    profile.objectif3a="Vous n'avez pas défini d'objectif"
    profile.objectif3b=""
    profile.objectif3c=""
    profile.save()
    return HttpResponseRedirect('/VosObjectifs/')

def coach(request):
    current_path=get_current_path(request)
    return render(request, 'coachPersonalise.html', {'current_path':current_path})

def monCompte(request):
    current_path=get_current_path(request)
    return render(request, 'monCompte.html', {'current_path':current_path})

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
