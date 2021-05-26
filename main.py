from typing import Text
import requests
import json
import keyboard
import tkinter as tk
def start():
    global stop
    stop = enty.get()
    window.destroy()
window = tk.Tk()
label = tk.Label(text="Swiss Train departure utility\n Please Enter Your station")
enty = tk.Entry(width=50)
B = tk.Button(text="OK", command= start)
label.pack()
enty.pack()
B.pack()
window.mainloop()


URL = "https://fahrplan.search.ch/api/stationboard.json?"
inf = {'stop': stop,
        'limit': '1'}
r = requests.get(url = URL, params= inf)
jsono = r.text
d = json.loads(jsono)
print(d["connections"][0]["line"])

