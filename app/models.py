from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Amis(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    travail = models.CharField(max_length=60)
    age = models.CharField(max_length=3)
    region = models.CharField(max_length=30)

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    photo = models.TextField()
    objectif = []
    objectif1 = models.CharField(max_length=10)
    objectif1a=models.CharField(max_length=30)
    objectif1b=models.CharField(max_length=30)
    objectif1c=models.CharField(max_length=30)
    objectif1d=models.CharField(max_length=30)




#old tutorial
# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title
