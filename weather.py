import requests
from config import WEATHER_API


s_city = 'Sochi'

class Weather:
    def __init__(self):
        self.api = WEATHER_API

    def new_weather(self):
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                               params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': self.api})
            data = res.json()
            temp = data["list"][0]["main"]["temp"]
            feels_like = data["list"][0]["main"]["feels_like"]
            temp_max, temp_min = data["list"][0]["main"]["temp_max"], data["list"][0]["main"]["temp_min"]
            pressure = data["list"][0]["main"]["pressure"]
            humidity = data["list"][0]["main"]["humidity"]
            wind_speed = data["list"][0]["wind"]["speed"]
            gradus = data["list"][0]["wind"]["deg"]
            value = f"Температура: {temp}\nОщущается как: {feels_like}\nМаксимальная температура сегодня: {temp_max}\n" \
                    f"Минимальая температура сегодня: {temp_min}\nДавление: {pressure}\nВлажность: {humidity}\n" \
                    f"Скорость ветра: {wind_speed}\nУклон ветра: {gradus}"
            return value
        except Exception as ex:
            print("Error:", ex)
            return 1

c = Weather()
print(c.new_weather())
