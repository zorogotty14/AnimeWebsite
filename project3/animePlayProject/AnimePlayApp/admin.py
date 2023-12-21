from django.contrib import admin

# Register your models here.
from .models import *
from mptt.admin import MPTTModelAdmin
admin.site.register(WatchList)
admin.site.register(AnimeCategory)
admin.site.register(Anime)
admin.site.register(Comment, MPTTModelAdmin)
