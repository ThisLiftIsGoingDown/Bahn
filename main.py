from tkinter.constants import COMMAND
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
window.title("Public transit Departure")
label = tk.Label(text="Swiss Train departure utility\n Please Enter Your station")
enty = tk.Entry(width=50)
B = tk.Button(text="OK", command= start)
label.pack()
enty.pack()
B.pack()
window.mainloop()

def start1():
    global numberOfStations
    numberOfStations = int(et.get())
    number.destroy()


number = tk.Tk()
number.title("Public Transit Departure")
nb = tk.Label(text="Please enter the number of entries you want to see:")
et = tk.Entry(width=50)
btt = tk.Button(text = "OK", command= start1)
nb.pack()
et.pack()
btt.pack()
number.mainloop()

print (stop)
URL = "https://fahrplan.search.ch/api/stationboard.json?"
inf = {'stop': stop,
        'limit': numberOfStations}
r = requests.get(url = URL, params= inf)
jsono = r.text
d = json.loads(jsono)
for i in range(0,numberOfStations ):
    print(d["connections"][i]["line"])

