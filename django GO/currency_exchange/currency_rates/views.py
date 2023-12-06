# currency_rates/views.py
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def currency_view(request):
    api_url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    response = requests.get(api_url)
    data = response.json()
    return render(request, 'main/currency_rates.html', {'currencies': data})
