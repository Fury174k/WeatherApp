import requests
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.messages import Message
from django.http import JsonResponse


# Create your views here.
def homePage(request):
    return render(request, 'home.html')

def roomPage(request):
    return render(request, 'room.html')

def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return render(request, 'home.html')
    else:
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    
def logoutUser(request):
    logout(request)
    return render(request, 'home.html')



def weather_form(request):
    return render(request, 'weather_form.html')



def get_weather(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        api_key = '2272ed8c8c5a7f05580ea3a049d71ff6'
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

        response = requests.get(url)
        data = response.json()

        return render(request, 'weather_result.html', {'data': data})
    return JsonResponse({'error': 'Invalid request'}, status=400)

