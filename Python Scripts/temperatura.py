import schedule
import time
import requests

class APIdata():
    def assitirTemp(latitude:int, longitude:int) -> int:
        url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m&daily=temperature_2m_max,temperature_2m_min&current_weather=true&timezone=America%2FSao_Paulo'
        response = requests.get(url)
        data = response.json()
        return data
    
    def enviar(dataWeather, celcius, isday, name):
        if(isday == 0):
            complement = f'Good night, {name}'
        else:
            complement = f'Good morning, {name}'

        initText = f'{complement}!\nNow temperature: {celcius}'
        return(initText)


    if __name__ == "__main__":
        dataWeather = assitirTemp(-19.747368, -47.939156)
        celcius = dataWeather["current_weather"]["temperature"]
        isday = dataWeather["current_weather"]["is_day"]
        show = enviar(dataWeather, celcius, isday, "Stark")
        print(show)