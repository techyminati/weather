#! /usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) TechyMinati ( Aryan Sinha ) <sinha.aryan03@gmail.com>

import requests
from pprint import pprint
API_Key = "105d997a8a1977cb138167503eb7afa1"
location = input("Enter Your Desired Location: ")
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
final_url = weather_url + API_Key
weather_data = requests.get(final_url).json()
pprint(weather_data)

