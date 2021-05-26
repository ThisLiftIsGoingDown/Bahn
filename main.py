import requests
import json
URL = "https://fahrplan.search.ch/api/stationboard.json?"
inf = {'stop':'Einsiedeln',
        'limit': '1'}
r = requests.get(url = URL, params= inf)
jsono = r.text
d = json.loads(jsono)
print(d["connections"][0]["terminal"]['name'])
