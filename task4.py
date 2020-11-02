import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("257x136")

#tophalf
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
p = tk.Label(window, text = "Pochacco!")

#bottomhalf
label2 = tk.Label(window, text = "A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg = "#87ceeb")


label1.place(x=60,y=0)
p.place(x=128.5, y=40)
label2.place(x=0, y=100)
window.mainloop()