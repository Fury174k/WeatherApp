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
        city = request.POST.get('city')
        api_key = 'PUT IN YOUR API KEY HERE'
        url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}'

        response = requests.get(url)
        data = response.json()
        
        if data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

            response = requests.get(url)
            weather_data = response.json()
            
            # Combine both data dictionaries into one context dictionary
            context = { 'city': city, 
                       'temperature': round(weather_data['main']['temp']- 273), 
                       'description': weather_data['weather'][0]['description'], 
                       'humidity': weather_data['main']['humidity'], 
                       'wind_speed': weather_data['wind']['speed'], 
                       }
        else:
            context = {'error': 'City not found'}
        
        return render(request, 'weather_result.html', context)
    return JsonResponse({'error': 'Invalid request'}, status=400)



