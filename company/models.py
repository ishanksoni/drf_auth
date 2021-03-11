from django.db import models
from django.contrib.auth.models import User

## Company Page Model
class Page(models.Model):
    user = models.ForeignKey(User, related_name= "page_owner", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=100) 
    about = models.TextField()

    def __str__(self):
        return self.name

## Follow Table  to record followers and company
class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="followings" ,on_delete= models.CASCADE) 
    following  = models.ForeignKey(Page, related_name= "followers", on_delete = models.CASCADE)

    def __str__(self):
        return self.follower.username