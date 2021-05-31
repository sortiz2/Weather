import requests
from pprint import pprint

key='594e90ce02964b4bf7d942ed63b3f6ca'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)