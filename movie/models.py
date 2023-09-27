from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE, related_name='movies_directed')
    avg_rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    actors = models.ManyToManyField('Actor', related_name='movies_acted')
    rating = models.ForeignKey('Rating', on_delete=models.SET_NULL, null=True, related_name='movies_rated')
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Rating(models.Model):
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return str(self.rating)