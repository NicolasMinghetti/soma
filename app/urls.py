from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^graphe$', views.graphe),
    url(r'^index$', views.index),
    url(r'^choisir', views.objectifChoisir),
    url(r'^name', views.name),
#    url(r'^form', views.form),
    url(r'^recherche$', views.recherche),
    url(r'^VosObjectifs/supprimer$', views.vosObjectifsSupprimer),
    url(r'^VosObjectifs', views.vosObjectifs),
    url(r'^coach$', views.coach),
    url(r'^monCompte$', views.monCompte),
    url(r'^objectif', views.objectif),
    url(r'^reseaux$', views.reseaux),
    url(r'^suggestions$', views.suggestions),
    url(r'^test_view$', views.test_view),
    url(r'^logout$', views.logout_view),
]
