#!python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")

#tophalf
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
p = tk.Label(window, text = "Pochacco!")

label1.grid(row = 1, column = 2, rowspan = 3, sticky = E)
p.grid(row = 2, column = 3, sticky = W)

#bottomhalf
label2 = tk.Label(window, text = "A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg = "#87ceeb")
label2.grid (row = 4, column = 1, columnspan = 4)

window.mainloop()