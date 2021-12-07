from django.urls import path
from .views import gameInformation, searchByName, bestGamesByPlatform, bestGamesByYear, bestGamesByGenre, best5GamesBySale, compareBySale

urlpatterns = [
    path('gameInformation/', gameInformation, name='gameInformation'),#http://127.0.0.1:8000/RestAPI/gameInformation/
    path('searchByName/', searchByName, name='searchByName'),  # http://127.0.0.1:8000/RestAPI/searchByName/
    path('bestGamesByPlatform/', bestGamesByPlatform, name='bestGamesByPlatform'),#http://127.0.0.1:8000/RestAPI/bestGamesByPlatform/
    path('bestGamesByYear/', bestGamesByYear, name='bestGamesByYear'),#http://127.0.0.1:8000/RestAPI/bestGamesByYear/
    path('bestGamesByGenre/', bestGamesByGenre, name='bestGamesByGenre'),  # http://127.0.0.1:8000/RestAPI/bestGamesByGenre/
    path('best5GamesBySale/', best5GamesBySale, name='best5GamesBySale'),  # http://127.0.0.1:8000/RestAPI/best5GamesBySale/
    path('compareBySale/', compareBySale, name='compareBySale'),  # http://127.0.0.1:8000/RestAPI/compareBySale/
    path('searchByName/', searchByName, name='searchByName'),  # http://127.0.0.1:8000/RestAPI/searchByName/
]