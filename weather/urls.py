from django.urls import path
from . import views

"""при переходе на новую страницу"""
urlpatterns = [
    path('', views.index),
]
