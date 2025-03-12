import requests
import datetime

api_geocoder = "1c1910a2-765e-4aeb-b635-a2d4d47691fa"

location_input = input("Где вы живете?\n")
response_location = requests.get(f"https://geocode-maps.yandex.ru/1.x/?apikey={api_geocoder}&geocode={location_input}&format=json")
location = response_location.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()

current_date = datetime.date.today()
date_plus_day = current_date + datetime.timedelta(days=1)
response_weather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location[0]}&longitude={location[1]}&current=temperature_2m,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=auto&start_date={current_date.isoformat()}&end_date={date_plus_day.isoformat()}")
weather_current = response_weather.json()["current"]
weather_tomorrow = response_weather.json()["daily"]

weather_code = {
    0: "Ясно",
    1: "Преимущественно ясно",
    2: "Переменная облачность",
    3: "Пасмурно",
    45: "Туман",
    48: "Иней",
    51: "Слабая морось",
    53: "Умеренная морось",
    55: "Плотная морось",
    56: "Слабый град",
    57: "Умеренный град",
    61: "Слабый дождь",
    63: "Умеренный дождь",
    65: "Плотный дождь",
    66: "Слабый ледяной дождь",
    67: "Плотный ледяной дождь",
    71: "Слабый снег",
    73: "Умеренный снег",
    75: "Плотный снег",
    77: "Снежные зерна",
    80: "Слабый ливень",
    81: "Умеренный ливень",
    82: "Плотный ливень",
    85: "Умеренный снегопад",
    86: "Плотный снегопад",
    95: "Гроза",
    96: "Слабая гроза",
    99: "Сильная гроза",}

current_temp = weather_current["temperature_2m"]
current_weather = weather_code[weather_current["weather_code"]]
daily_temp = weather_tomorrow["temperature_2m_min"][1] + weather_tomorrow["temperature_2m_max"][1] / 2
daily_weather = weather_code[weather_tomorrow["weather_code"][1]]
print()
print(f"'{location_input}'\nНа данный момент:\nТемпература: {current_temp}°C\nПогода: {current_weather}\n\nНа следующий день:\nСредняя температура: {daily_temp}°C\nПогода: {daily_weather}")