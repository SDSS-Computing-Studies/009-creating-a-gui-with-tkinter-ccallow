#!python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()

label1 = tk.Label(window,text="x")
button1 = tk.Button(window,text="=")
entry1 = tk.Entry(window, borderwidth=3)
entry2 = tk.Entry(window, borderwidth=3)
entry3 = tk.Entry(window, borderwidth=3)

entry1.grid (row = 1, column = 1)
label1.grid (row = 1, column = 2)
entry2.grid (row = 1, column = 3)
button1.grid (row = 1, column =4)
entry3.grid (row = 1, column = 5)

window.mainloop()