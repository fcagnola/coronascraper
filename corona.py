#!/usr/bin/env python3

from datetime import date, timedelta
import requests
import csv
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

_BASE_URL = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv"

class Data:
    def __init__(self):
        self.fetch_data()

    def fetch_data(self):
        response = requests.get(_BASE_URL)
        reader = csv.DictReader(response.text.splitlines())
        data = {'nuovi_positivi':0, "tamponi":0}
        for row in reader:
            data['nuovi_positivi'] += int(row['nuovi_positivi'])
            data['tamponi'] += int(row['tamponi'])
            data[row['denominazione_regione']] = {'nuovi_positivi':int(row['nuovi_positivi']), "tamponi":int(row['tamponi'])}
        self.data = data

    def nazionali(self):   
        msg = f"{Fore.CYAN}Nuovi casi in Italia: {self.data['nuovi_positivi']}\nTestati: {self.data['tamponi']}"
        return msg

    def regione(self, regione):  
        msg = f"{Fore.CYAN}Nuovi casi in {regione.title()}: {self.data[regione.title()]['nuovi_positivi']}\nTestati: {self.data[regione.title()]['tamponi']}"
        return msg


# shell call will look like this: python3 corona.py {country name /or/ world}

data = Data()
print(data.nazionali())
print(data.regione("lombardia"))

