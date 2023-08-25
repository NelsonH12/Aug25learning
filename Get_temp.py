import daytime as dt
import requests

base_url = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = open('api_key.txt', 'r').read()
city = input("From which city do you need the temperature? ")

def kelvin_to_c_f(kelvin):
  celsius = kelvin - 273.15
  fahrenheit = celsius * (9/5) + 32
  return celsius, fahrenheit

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_c_f(temp_kelvin)
feels_like_kelvin = response ['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_c_f(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']

print(f'Temperature in {city}: {temp_celsius:.2f}*C or {temp_fahrenheit}*F')