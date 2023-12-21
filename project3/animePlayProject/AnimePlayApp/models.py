from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel,TreeForeignKey


# Create your models here.
class Anime(models.Model):
    name = models.TextField()
    aired = models.TextField()
    studios = models.TextField(max_length=200)
    type = models.CharField(max_length=200,default='series')
    description = models.TextField()
    img = models.TextField()
    video = models.TextField()

class AnimeCategory(models.Model):
    type = models.TextField()

class WatchList(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    username = models.TextField(default=0)
    name = models.TextField(default=0)
    aired = models.TextField(default=0)
    studios = models.TextField(max_length=200,default=0)
    type = models.CharField(max_length=200, default='series')
    description = models.TextField(default=0)
    img = models.TextField(default=0)
    video = models.TextField(default=0)

class Comment(MPTTModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='children')
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return self.name

new_User = { "username": "name", "password": "text1234@"}
admin_User = { "username": "name", "password": "Abcd1234!"}