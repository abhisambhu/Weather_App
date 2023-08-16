from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=931e6a32c10f27106addc48b6ddda851"
    # city = 'London'
    # key='931e6a32c10f27106addc48b6ddda851'
    if request.method == 'POST':
        form =CityForm(request.POST)
        form.save()
    form=CityForm()

    cities = City.objects.all()
    weather_data=[]
    for city in cities:

        r = requests.get(url.format(city)).json()
        city_weather={
            'city':city,
            'temperature': r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = {'city_weather': city_weather,'form':form}
    return render(request,'weather/weather.html',context)