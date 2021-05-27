import requests
from tkinter import *
import json
def Wayfinder():
    def bttnAct():
        global fr
        fr = enty.get()
        von.destroy()

    von = Tk()
    von.title("Public Transport Route Finder")
    label = Label(text="Public transport route finder\n Please Enter Your Departure station")
    enty = Entry(width=50)
    B = Button(text="OK", command= bttnAct)
    label.pack()
    enty.pack()
    B.pack()
    von.mainloop()

    def bttnAct1():
        global to
        to = entyt.get()
        nach.destroy()

    nach = Tk()
    nach.title("Public Transport Route Finder")
    label = Label(text="Public transport route finder\n Please Enter Your Arrival station")
    entyt = Entry(width=50)
    B = Button(text="OK", command= bttnAct1)
    label.pack()
    entyt.pack()
    B.pack()
    nach.mainloop()

    URL = "https://fahrplan.search.ch/api/route.json?"
    inf = {'from': fr,
            'to': to,
            'num': '1'}
    r = requests.get(url = URL, params= inf)
    jsono = r.text
    d = json.loads(jsono)

    master = Tk()
    infes =Text(master, height=15, width= 110)
    bar = Scrollbar(master)
    bar.pack(side=RIGHT)
    infes.pack()
    frotmp = str(d["connections"][0]["from"])
    totmp = str(d["connections"][0]["to"])
    depttmp = str(d["connections"][0]["departure"])
    arrttmp = str(d["connections"][0]["arrival"])
    conn = f"Your connection from: {frotmp} to: {totmp}:\nDeparture: {depttmp}\nArrival: {arrttmp}\n"
    ergebnis = ""
    for i, leg in enumerate(d["connections"][0]["legs"]):
        tmpstr = ""
        if i < len(d["connections"][0]["legs"])-1:
            firsttempbin = ""
            firsttempexit = str(leg["exit"]["name"])
            firsttemp = str(leg["name"])
            try:
                firsttempline = str(leg["line"])
            except:
                firsttempline = "-"
            firsttemptime= str(leg["departure"])
            try:
                firsttempterminal = str(leg["terminal"])
            except: 
                firsttempterminal = "-"
            try:
                firsttempbin = str(leg["track"])
            except:
                firsttempbin = "-"
            firsttempbin = f"from track nr.{firsttempbin}"
            tmpstr = f"In {firsttemp} take the {firsttempline} in driection of {firsttempterminal} to {firsttempexit} {firsttempbin} at {firsttemptime}\nThen:\n"
        else:
            firsttemp = str(leg["name"])
            firsttemptime= str(leg["arrival"])
            tmpstr = f"You arrive in {firsttemp} at {firsttemptime}"
        ergebnis+= tmpstr
    print (ergebnis)
    infes.insert(END, ergebnis)
    mainloop()
    return None