"""для считывания температуры у множества других городов. City - табличка"""
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)

    "метод __str__, который будет возвращать не объект, а само значение в табличке, т.е. название самого города."
    def __str__(self):
        return self.name
