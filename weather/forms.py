"""этот файл нужен для того, чтобы
можно было записать любой город, узнать о нем
информацию и, чтобы эта информация записалась в
базу данных и отобразилась на экране"""
from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город'
        })}
