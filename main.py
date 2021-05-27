import DepBoard
import Wayfinder
from tkinter import *

def Wayfind():
    haupt.destroy()
    Wayfinder.Wayfinder()

def Dep():
    haupt.destroy()
    

haupt = Tk()
haupt.title("Public Transport")
label = Label(text="Please Click the utility you want to use")
A = Button(text="Departure Board", command=Dep)
B = Button(text="Route Planer", command= Wayfind)
label.pack()
A.pack()
B.pack()
haupt.mainloop()