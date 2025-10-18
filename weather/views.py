from django.shortcuts import render
import requests, os
from django.conf import settings


def home(request):
    city = request.GET.get('city', 'London')
    api_key = os.getenv("OWM_API_KEY") or getattr(settings, "OWM_API_KEY", None)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    context = {}

    if data.get("cod") != "404":
        context = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }

    return render(request, "weather/index.html", context)


def about(request):
    return render(request, "weather/about.html")


def contact(request):
    return render(request, "weather/contact.html")
