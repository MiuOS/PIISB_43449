from django.http import JsonResponse
from .models import Movie, Actor, Rating
from .serializers import MovieSerializer, ActorSerializer, RatingSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('title')
        title = request.query_params.get('title', None)
        if title:
            movies = movies.filter(title__icontains=title)
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse({'movies': serializer.data}, safe=False)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors)

@api_view(['GET', 'PUT'])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return JsonResponse({'message': 'The movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data, partial=True)  # partial=True allows partial update
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all().order_by('name')
        name = request.query_params.get('name', None)
        if name:
            actors = actors.filter(name__icontains=name)
        serializer = ActorSerializer(actors, many=True)
        return JsonResponse({'actors': serializer.data}, safe=False)
    
    if request.method == 'POST':
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors)

@api_view(['GET', 'POST'])
def rating_list(request):
    if request.method == 'GET':
        ratings = Rating.objects.all().order_by('rating')
        rating = request.query_params.get('rating', None)
        if rating:
            ratings = ratings.filter(rating=rating)
        serializer = RatingSerializer(ratings, many=True)
        return JsonResponse({'ratings': serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors)