from tkinter.constants import COMMAND, RIGHT
from typing import Text
import requests
import json
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
        'limit': numberOfStations,
        'show_delays': '1',
        'show_subsequent_stops': '1'}
r = requests.get(url = URL, params= inf)
jsono = r.text
d = json.loads(jsono)
results = tk.Tk()
results.title("Public Transit Departure")
bar = tk.Scrollbar(results)
bar.pack(side=RIGHT)
rqstation =  d["stop"]["name"]
departures = f"\nDepartures from {rqstation}:\n"
for i in range(0,numberOfStations ):
    tmpstr = ""
    tmptype = d["connections"][i]["type"]
    tmpline = d["connections"][i]["line"]
    tmpdest = d["connections"][i]["terminal"]["name"]
    try:
        tmpdel = d["connections"][i]["dep_delay"]
    except:
        tmpdel = "No Delay Info Available"
    tmptime = d["connections"][i]["time"]
    tmpstr = f"\nLine: {tmpline}\nDep.time: {tmptime}\nTo: {tmpdest}\nType: {tmptype}\nDelay: {tmpdel}\nStops at:\n"
    tmpstr1 = ""
    for cazzo in range (0,len(d["connections"][i]["subsequent_stops"])): #Sorry to all italian speaking people for the variable name
        dudidu =str(d["connections"][i]["subsequent_stops"][cazzo]["name"])
        tmpstr1 += f"{dudidu}\n"
    tmpstr += tmpstr1
    print(tmpstr)
    departures += tmpstr
lab = tk.Label(text= departures)
lab.pack()
results.mainloop()