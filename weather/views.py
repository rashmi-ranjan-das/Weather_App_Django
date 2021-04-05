from django.shortcuts import render
import requests
import json
import datetime

# Create your views here.
def home(request):
    # data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Bhubaneswar&appid=fc739effd09689c4c3ca4c4f22ab7ab4")
    # data = data.json()
    # print(data['weather'][0]['main'])
    return render(request, 'weather/home.html')

def details(request):
    place = request.GET['place']
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid=fc739effd09689c4c3ca4c4f22ab7ab4")
    data = data.json()
    try:
        name = data['name']
        country = data['sys']['country']
        capital_name = name.upper()
        wind_speed = data['wind']['speed']
        temp = int(data['main']['temp'] - 273.15)
        cloudiness = data['clouds']['all']
        temp_feel = int(data['main']['feels_like'] - 273.15)
        min_temp = data['main']['temp_min'] - 273.15
        max_temp = data['main']['temp_max'] - 273.15
        humidity = data['main']['humidity']
        weather_type = data['weather'][0]['main']
        final_data = {
            'name': name,
            'country': country,
            'wind_speed' : wind_speed,
            'temp' : temp,
            'clouds': cloudiness,
            'temp_feel': temp_feel,
            'min_temp' : min_temp,
            'max_temp' : max_temp,
            'humidity' : humidity,
            'weather_type': weather_type,
            'time': datetime.datetime.now().strftime("%H:%M:%S")
        }
        return render(request, 'weather/details.html', {'final_data':final_data})
    except:
        final_data = {
            'name': request.GET['place'].upper(),
            'country': "",
            'wind_speed' : "",
            'temp' : "",
            'clouds': "",
            'temp_feel': "",
            'min_temp' : "",
            'max_temp' : "",
            'humidity' :  "",
            'weather_type': "",
            'time': datetime.datetime.now().strftime("%H:%M:%S")
        }
        return render(request, 'weather/details.html', {'final_data':final_data})