from django.urls import path
from .views import uf_single_date_view

urlpatterns = [
    path('uf/<str:fecha>/', uf_single_date_view, name='uf_single_date_view'),
]