import tkinter as tk
from tkinter import ttk
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cal_path = os.path.join(BASE_DIR, "calendar-icon.gif")

def calendarButton(container):
    button = ttk.Button(container,width=30)
    photo = tk.PhotoImage(file=cal_path)
    button.config(image=photo)
    button.image = photo
    return button
