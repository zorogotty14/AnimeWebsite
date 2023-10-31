from django.contrib import admin

# Register your models here.
from .models import * 
admin.site.register(WatchList)
admin.site.register(Customer)
admin.site.register(AnimeCategory)
admin.site.register(Anime)
