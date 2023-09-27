from rest_framework import serializers
from .models import Movie, Actor, Rating, Director

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'director', 'avg_rating', 'created_at', 'updated_at', 'director', 'rating', 'slug']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'bio']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'bio']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rating', 'created_at', 'updated_at', 'user']