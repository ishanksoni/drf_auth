from django.db import models
from django.contrib.auth.models import User

class UserManager(models.Manager):
    M = 0
    F = 1
    GENDER_CHOICES = [(M, 'Male'), (F, 'Female')]
    def males(self):
        return self.all().filter(gender=self.M)
    def females(self):
        return self.all().filter(gender=self.F)

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    gender = models.IntegerField(choices=UserManager.GENDER_CHOICES)
    dob = models.DateField()
    about = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username
