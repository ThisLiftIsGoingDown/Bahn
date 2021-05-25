import json
import requests

data = requests.get("http://transport.opendata.ch/v1/stationboard?station=Riehen,%20Bahnhof")
print(data)
print("1")