import requests

response = requests.get('http://localhost:8000/movies')
print(response.json())