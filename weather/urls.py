from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('weather/', views.weather_form, name='weather_form'),
    path('api/get_weather/', views.get_weather, name='get_weather'),
]
