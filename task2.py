#!python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")


#tophalf
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
button1 = tk.Button(window,text="Search by Name")
entry1 = tk.Entry(window)
label2 = tk.Label(window, text="Client Database")



label1.grid(row = 1, column = 1, rowspan = 3)
button1.grid(row = 1, column = 4)
entry1.grid(row = 1, column = 5)
label2.grid(row =2, column = 3)

#middle
name = tk.Label(window, text = "Name")
nentry = tk.Entry(window, borderwidth = 3)
typeo = tk.Label(window, text = "Type")
tentry = tk.Entry (window, borderwidth = 3)
breed = tk.Label(window, text = "Breed")
bentry = tk.Entry (window, borderwidth = 3)
owner = tk.Label(window, text = "Name")
oentry = tk.Entry(window, borderwidth = 3)
bd = tk.Label(window, text = "Birthdate")
bdentry = tk.Entry(window, borderwidth = 3)

name.grid(row = 4, column = 1)
nentry.grid(row = 5, column = 1)
typeo.grid(row = 4, column = 2)
tentry.grid(row = 5, column =2)
breed.grid(row = 4, column = 3)
bentry.grid (row = 5, column = 3)
owner.grid(row = 4, column = 4)
oentry.grid (row = 5, column = 4)
bd.grid(row = 4, column = 5)
bdentry.grid(row =5, column = 5)

#bottomhalf
button2 = tk.Button(window,text="< Previous")
save = tk.Button(window, text = "Save Entry")
button3 = tk.Button(window, text = "Next >")

button2.grid(row  = 6, column = 1, sticky = W)
save.grid(row = 6, column = 3)
button3.grid (row = 6, column = 5, sticky = E)



window.mainloop()