from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#comes from tutorial :
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

class UserProfile(models.Model):
    #on link a l user :
    user = models.OneToOneField('auth.User', related_name='userprofile')
    # user = models.ForeignKey(User, unique=True)
    #data recuperee de facebook :
    facebook_access_token = models.CharField(max_length=255)
    locale = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    facebook_link = models.CharField(max_length=30)
    facebook_id = models.CharField(max_length=30)

    # User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
    #
    # def __unicode__(self):
    #     return self.profile
