from django.test import TestCase
from .models import Movie, Director, Actor  # adjust the import as per your project structure

class MovieCreationTest(TestCase):

    def setUp(self):
        # Create a director for the movie
        self.director = Director.objects.create(
            name='Jane Doe',
            bio='A renowned director.'
        )
        
        # Create an actor for the movie
        self.actor = Actor.objects.create(
            name='John Doe',
            bio='An experienced actor.'
        )

    def test_create_movie(self):
        movie = Movie.objects.create(
            title='Test Movie',
            description='A great movie',
            year=2023,
            director=self.director,
            avg_rating=5.0
        )
        
        # Adding an actor to the movie
        movie.actors.add(self.actor)
        
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(movie.title, 'Test Movie')
        self.assertIn(self.actor, movie.actors.all())
        self.assertEqual(movie.director, self.director)

from django.test import TestCase
from .models import Movie, Director, Actor  # adjust the import as per your project structure

class GetTest(TestCase):

    def setUp(self):
        self.director = Director.objects.create(
            name='Jane Doe',
            bio='A renowned director.'
        )
        
        self.actor = Actor.objects.create(
            name='John Doe',
            bio='An experienced actor.'
        )
        
        self.movie_title = 'Test Movie'
        self.movie = Movie.objects.create(
            title=self.movie_title,
            description='A great movie',
            year=2023,
            director=self.director,
            avg_rating=5.0
        )
        self.movie.actors.add(self.actor)

    def test_get_movie_by_title(self):
        retrieved_movie = Movie.objects.get(title=self.movie_title)
        self.assertEqual(retrieved_movie.title, self.movie_title)
        self.assertEqual(retrieved_movie, self.movie)  # additionally, you can check if the retrieved movie is the same as the created one
