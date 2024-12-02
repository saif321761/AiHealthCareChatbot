# Chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Path for the index view
]
