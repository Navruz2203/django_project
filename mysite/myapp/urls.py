from django.contrib import admin
from django.urls import path

from myapp.views import detail, index

app_name = 'myapp'

urlpatterns = [
    path('', index, name="home"),
    path('detail/<int:product_id>/', detail, name='detail')
]
