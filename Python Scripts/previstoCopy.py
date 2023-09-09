import schedule
import time
import requests
    
def WhatchWeather(latitude, longitude):

    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m&daily=temperature_2m_max,temperature_2m_min&current_weather=true&timezone=America%2FSao_Paulo'
    response = requests.get(url)
    data = response.json()
    return data

def send():

    name = "NAME" #change here your name
    latitude = -19.7483
    longitude = -47.9319

    dataWeather = WhatchWeather(latitude, longitude)
    celcius = dataWeather["current_weather"]["temperature"]
    isday = dataWeather["current_weather"]["is_day"]

    complement = ""

    if(isday == 0):
        complement = f'Good night, {name}'
    else:
        complement = f'Good morning, {name}'

    initText = f'{complement}!\nNow temperature: {celcius}'
    print(initText)
    
send()