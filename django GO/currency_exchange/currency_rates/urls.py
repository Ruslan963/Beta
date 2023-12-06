# currency_rates/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.currency_view, name='currency_view'),
]
