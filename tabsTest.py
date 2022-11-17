import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import json
import io
import os
from PIL import Image, ImageTk
import PySimpleGUI as sg
import cloudscraper
import urllib
import datetime
import main

window = tk.Tk()
window.title("Beat Saber Score Comparator")
tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Recent Players')
tabControl.add(tab2, text='Leaderboard')
tabControl.add(tab3, text='Graph')
tabControl.pack(expand=1, fill="both")

ttk.Label(tab1,
          text="Recent Players").grid(column=0,
                               row=0,
                               padx=30,
                               pady=30)
ttk.Label(tab2,
          text="Leaderboard").grid(column=0,
                                    row=0,
                                    padx=30,
                                    pady=30)

ttk.Label(tab3,
          text="Graph").grid(column=0,
                                    row=0,
                                    padx=30,
                                    pady=30)

window.mainloop()