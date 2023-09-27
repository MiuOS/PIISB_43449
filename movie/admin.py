from django.contrib import admin
from .models import Movie, Actor, Rating, Director

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Rating)