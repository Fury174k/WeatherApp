from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name='home'),
    path('room/', views.roomPage, name='room'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('weather/', views.weather_form, name='weather_form'),
    path('get_weather/', views.get_weather, name='get_weather'),
]
