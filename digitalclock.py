from tkinter import *
from tkinter.ttk import *

from time import strftime
root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
label=Label(root,font=("Timesnewroman",50),background="black",foreground="green")
label.pack(anchor='center')
time()

mainloop()
