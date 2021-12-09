from django.urls import path
from .views import GameInformation, SearchByName, BestGamesByPlatform, BestGamesByYear, BestGamesByGenre, Best5GamesBySale, CompareBySale

urlpatterns = [
    path('gameInformation/', GameInformation.as_view(), name='gameInformation'),#http://127.0.0.1:8000/RestAPI/gameInformation/
    path('searchByName/', SearchByName.as_view(), name='searchByName'),  # http://127.0.0.1:8000/RestAPI/searchByName/
    path('bestGamesByPlatform/', BestGamesByPlatform.as_view(), name='bestGamesByPlatform'),#http://127.0.0.1:8000/RestAPI/bestGamesByPlatform/
    path('bestGamesByYear/', BestGamesByYear.as_view(), name='bestGamesByYear'),#http://127.0.0.1:8000/RestAPI/bestGamesByYear/
    path('bestGamesByGenre/', BestGamesByGenre.as_view(), name='bestGamesByGenre'),  # http://127.0.0.1:8000/RestAPI/bestGamesByGenre/
    path('best5GamesBySale/', Best5GamesBySale.as_view(), name='best5GamesBySale'),  # http://127.0.0.1:8000/RestAPI/best5GamesBySale/
    path('compareBySale/', CompareBySale.as_view(), name='compareBySale'),  # http://127.0.0.1:8000/RestAPI/compareBySale/
    path('searchByName/', SearchByName.as_view(), name='searchByName'),  # http://127.0.0.1:8000/RestAPI/searchByName/
]