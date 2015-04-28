from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^graphe$', views.graphe),
    url(r'^index$', views.index),
    url(r'^objectif', views.objectif),
    url(r'^reseaux$', views.reseaux),
    url(r'^suggestions$', views.suggestions),
    url(r'^test_view$', views.test_view),
    url(r'^logout$', views.logout_view),
]
