from django.urls import path
from . import views

"""при переходе на главную страницу, используем файл views и в нем 
функцию index"""
urlpatterns = [
    path('', views.index),
]
