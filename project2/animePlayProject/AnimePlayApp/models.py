from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Anime(models.Model):
    name = models.TextField()
    aired = models.TextField()
    studios = models.TextField()
    description = models.TextField()
    img = models.TextField()
    video = models.TextField()

class AnimeCategory(models.Model):
    type = models.TextField()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class WatchList(models.Model):
    name = models.TextField()
    aired = models.TextField()
    studios = models.TextField()
    description = models.TextField()
    img = models.TextField()
    video = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)


new_User = { "username": "test", "password": "text1234@"}
admin_User = { "username": "test12", "password": "Abcd1234!"}