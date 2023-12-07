# myapp/views.py
from django.shortcuts import render
import requests

def currency_rates(request):
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    rates = response.json()
    return render(request, 'main/currency_rates.html', {'rates': rates})
