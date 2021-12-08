from django.urls import path
from .views import compareSales, compareSalesByYear, comparePublisherSales, compareSalesByGenre

urlpatterns = [
    path('compareSales/', compareSales, name='compareSales'),#http://127.0.0.1:8000/DataAnalysis/compareSales/
    path('compareSalesByYear/', compareSalesByYear, name='compareSalesByYear'),#http://127.0.0.1:8000/DataAnalysis/compareSalesByYear/
    path('comparePublisherSales/', comparePublisherSales, name='comparePublisherSales'),#http://127.0.0.1:8000/DataAnalysis/comparePublisherSales/
    path('compareSalesByGenre/', compareSalesByGenre, name='compareSalesByGenre'),#http://127.0.0.1:8000/DataAnalysis/compareSalesByGenre/
]