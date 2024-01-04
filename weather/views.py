import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

"здесь отображается файл"


def index(request):
    appid = 'dc44824f5dd32c90b4dd214c6d4723cb'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    """clean forms"""
    form = CityForm()

    """выбор всех данных из таблички"""
    cities = City.objects.all()
    """перебираем массив, который будет содержать данные о всех городах"""

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        """после чего, все записываетсяв наш массив"""
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
