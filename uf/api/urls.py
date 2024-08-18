from django.urls import path
from .views import uf_single_date_view
from .views import uf_month_view

urlpatterns = [
    path('uf/<str:fecha>/', uf_single_date_view, name='uf_single_date_view'),
    path('uf/<int:mes>/<int:anio>/', uf_month_view, name='uf_month_view'),
]