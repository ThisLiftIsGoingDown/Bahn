import json, requests
data = requests.get("http://transport.opendata.ch/v1/stationboard?station=Riehen,%20Bahnhof").text
print(data)