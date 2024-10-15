from django.contrib import admin
from django.urls import path

from myapp.views import index


urlpatterns = [
    path('', index)
]
