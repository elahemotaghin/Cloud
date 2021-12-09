from django.urls import path
from .views import CompareSales, ComparePublisherSales, CompareSalesByGenre, CompareSalesByYear

urlpatterns = [
    path('compareSales/', CompareSales.as_view(), name='compareSales'),#http://127.0.0.1:8000/DataAnalysis/compareSales/
    path('compareSalesByYear/', CompareSalesByYear.as_view(), name='compareSalesByYear'),#http://127.0.0.1:8000/DataAnalysis/compareSalesByYear/
    path('comparePublisherSales/', ComparePublisherSales.as_view(), name='comparePublisherSales'),#http://127.0.0.1:8000/DataAnalysis/comparePublisherSales/
    path('compareSalesByGenre/', CompareSalesByGenre.as_view(), name='compareSalesByGenre'),#http://127.0.0.1:8000/DataAnalysis/compareSalesByGenre/
]