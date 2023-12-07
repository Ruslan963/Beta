# yourproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('currency/', include('currency_rates.urls')),  # Підключаємо URL-шляхи з вашого додатку
]
