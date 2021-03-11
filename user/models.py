from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from company.models import Follow,Page


## User manage to manage gender field 
## extandable for managing password fields etc...
class UserManager(models.Manager):
    M = 0
    F = 1
    GENDER_CHOICES = [(M, 'Male'), (F, 'Female')]
    def males(self):
        return self.all().filter(gender=self.M)
    def females(self):
        return self.all().filter(gender=self.F)


##Profile model with oneToOne relation with User Table.
class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    gender = models.IntegerField(choices=UserManager.GENDER_CHOICES)
    dob = models.DateField()
    about = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username



## Create Tokens for User who registar Using Signals
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        user = instance
        Token.objects.create(user=instance)
        print(user.username ,"Token Created!!")

## Send Signal to deflaut Follow the App company Page
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def default_follow(sender, instance=None, created=False, **kwargs):
    if created:
        print("Registration Success \n You Started Following XYZ ")
        user = instance
        Follow.objects.create(follower = user, following=Page.objects.get(name = "XYZ"))
