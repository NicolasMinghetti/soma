from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    photo = models.TextField()
    objectif = []
    objectif1 = models.CharField(max_length=10)
    objectif1a=models.CharField(max_length=30)
    objectif1b=models.CharField(max_length=30)
    objectif1c=models.CharField(max_length=30)
    objectif2 = models.CharField(max_length=10)
    objectif2a=models.CharField(max_length=30)
    objectif2b=models.CharField(max_length=30)
    objectif2c=models.CharField(max_length=30)
    objectif3 = models.CharField(max_length=10)
    objectif3a=models.CharField(max_length=30)
    objectif3b=models.CharField(max_length=30)
    objectif3c=models.CharField(max_length=30)

class ChoixDeObjectif(models.Model):
    objectifa = models.CharField(max_length=10)
    objectifb = models.CharField(max_length=30)
    objectifc = models.CharField(max_length=30)
    objectifd = models.CharField(max_length=30)

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
