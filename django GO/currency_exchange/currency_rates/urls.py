from django.urls import path
from . import views

urlpatterns = [
    path('', views.currency_rates, name='currency_rates'),
]