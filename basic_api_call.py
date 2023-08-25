import daytime as dt
import requests

base_url = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = open('api_key.txt', 'r').read()
city = 'Pittsburgh'

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

print(response)
#if you leave the program here, it'll produce a list of available variables.