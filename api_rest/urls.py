
from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.getUsers, name='get_all_users'),
]
