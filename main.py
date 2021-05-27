import DepBoard
import Wayfinder
from tkinter import *

def Wayfind():
    haupt.destroy()
    Wayfinder.Wayfinder()

def Dep():
    haupt.destroy()
    

haupt = Tk()
haupt.title("Public Transport Route Finder")
label = Label(text="Public transport route finder\n Please Enter Your Departure station")
A = Button(text="Departure Board", command=Dep)
B = Button(text="Route Planer", command= Wayfind)
label.pack()
B.pack()
haupt.mainloop()