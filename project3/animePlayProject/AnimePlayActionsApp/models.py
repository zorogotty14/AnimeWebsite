from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
# Create your models here.

#activity stream model
class Action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verb = models.TextField(max_length=250)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.verb

    def get_absolute_url(self):
        if 'Deleted the user' in self.verb:
            return reverse('AnimePlayApp:index')
        elif 'profile' in self.verb:
            username = self.verb.split(' ')[-1]
            return reverse('AnimePlayApp:profile', args=[username])
        elif 'watchlist' in self.verb:
            return reverse('AnimePlayApp:watchlist')
        elif 'comment' in self.verb:
            animeid = self.verb.split(' ')[-3]
            return reverse('AnimePlayApp:detail', args=[animeid])
        elif 'deleted from animeDB' in self.verb:
            return reverse('AnimePlayApp:index')
        elif 'animeDB' in self.verb:
            animeid = self.verb.split(' ')[-1]
            return reverse('AnimePlayApp:detail', args=[animeid])
        else:
            return reverse('AnimePlayApp:index')
