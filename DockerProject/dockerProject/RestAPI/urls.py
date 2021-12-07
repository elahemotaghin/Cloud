from django.urls import path
from .views import gameInformation, bestGamesByPlatform

urlpatterns = [
    path('gameInformation/', gameInformation, name='gameInformation'),#http://127.0.0.1:8000/RestAPI/gameInformation/
    path('bestGamesByPlatform/', bestGamesByPlatform, name='bestGamesByPlatform'),#http://127.0.0.1:8000/RestAPI/bestGamesByPlatform/
]