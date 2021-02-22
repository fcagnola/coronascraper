#!/usr/bin/env python3

from api_parsehub import *
import sys
import requests
import json
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Data:
    def __init__(self, api_key, proj_token):
        self.api_key = api_key
        self.proj_token = proj_token
        self.params = {
            "api_key": self.api_key
        }
        self.last_data()

    def update(self):           # Updates ParseHub data, requesting updated parse
        response = requests.post(API_UPDATE_URL, self.params)
        self.data = json.loads(response.text)

    def last_data(self):        # Fetches most recent data and assigns it to self.data
        response = requests.get(API_GET_URL, self.params)
        self.data = json.loads(response.text)

    def world_cases(self):      # Returns World Cases
        d = self.data["world_stats"]
        for content in d:
            if content["name"] == "Coronavirus Cases:":
                msg = f"{Fore.CYAN}New worldwide cases: {content['value']}"
                return msg

    def country(self, country):  # Returns country-specific cases and tests
        d = self.data["country"]
        for content in d:
            if content["country_name"].lower() == country.lower():
                msg = "{}New cases in {}: {} \nTests in {}: {}".format(Fore.CYAN, country.title(), content['new_cases'], country.title(), content['daily_tests'])
                return msg
        return Fore.RED + "error: gnò popo ffatta"


# shell call will look like this: python3 corona.py {country name /or/ world}

data = Data(API_KEY, PROJ_TOKEN)


if len(sys.argv) >= 1:
    if sys.argv[1] == "update":
        data.update()
        print("Update requested to Parsehub's API")
    else:
        country_input_name = sys.argv[1]
        print(f"Fetching data for {Fore.YELLOW}{country_input_name.title()}")
        if country_input_name.lower() != "world":
            d = data.country(country_input_name)
            print(d)
        else:
            d = data.world_cases()
            print(d)
else:
    d = data.world_cases()
    print(d)


