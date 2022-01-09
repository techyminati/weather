#! /usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) TechyMinati ( Aryan Sinha ) <sinha.aryan03@gmail.com>

import requests,json
from pprint import pprint
API_Key = "105d997a8a1977cb138167503eb7afa1" # Api Key fair use only
location = input("Enter Your Desired Location: ")
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
final_url = weather_url + API_Key
weather_data = requests.get(final_url).json()
# pprint(weather_data) // stop printing it here, better we will parse json

response = requests.get(final_url)
# check status of request
if response.status_code == 200: # parse the json now
   data = response.json()
   main = data['main']
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
   feels_like = main['feels_like']
   report = data['weather']
   sys = data['sys']
   country = sys['country']
   print(f"{location:-^30}")
   print(f"Country: {country}")
   print(f"Temperature: {temperature} F")
   print(f"Feels Like: {feels_like} F")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:  # Display a message if no response
   print("Error in the HTTP request, try again later!")

