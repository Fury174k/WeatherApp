from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.messages import Message
from django.http import JsonResponse
from django.conf import settings
import requests
from django.views.decorators.csrf import csrf_exempt

# Hardcoding the API key directly in the view
API_KEY = "2272ed8c8c5a7f05580ea3a049d71ff6"

# Create your views here.
def homePage(request):
 
    return render(request, 'home.html',)



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


@csrf_exempt
def get_weather(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        city = data.get("city")
        api_key = API_KEY  # Use the hardcoded API key

        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"
        geo_resp = requests.get(geo_url)
        geo_data = geo_resp.json()
        if not geo_data:
            return JsonResponse({"error": "City not found"}, status=404)
        latitude = geo_data[0]["lat"]
        longitude = geo_data[0]["lon"]
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
        weather_resp = requests.get(weather_url)
        weather_data = weather_resp.json()
        return JsonResponse(weather_data)
    return JsonResponse({"error": "Invalid request"}, status=400)






