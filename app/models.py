from django.db import models
from django.utils import timezone
<<<<<<< HEAD
=======
from django.contrib.auth.models import User
>>>>>>> 4a019b9aef590ef3439be748c275eeaaafae660d

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
<<<<<<< HEAD
=======

class UserProfile(models.Model):
    #on link a l user :
    user = models.OneToOneField(User)
    #data recuperee de facebook :
    facebook_access_token = models.CharField(max_length=255)
    locale = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    facebook_link = models.CharField(max_length=30)
    facebook_id = models.CharField(max_length=30)
>>>>>>> 4a019b9aef590ef3439be748c275eeaaafae660d
