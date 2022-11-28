import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from tkinter import Tk, Canvas, Listbox, Entry, Text, Button, PhotoImage, END, Frame

import requests
import re
from urlextract import URLExtract

from .PlayerPanel.ViewPanelFrame import ViewPlayer
from .EditPanel.EditPanelFrame import EditPlayer

import api

class PlayerWidget1(Frame):
    def __init__(self, player, parent, playerHex, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.player = player
        self.playerHex = playerHex

        self.configure(bg="#343638")

        # Loop through windows and place them
        self.windows = {
            "view": ViewPlayer(self, self.playerHex),
            "edit": EditPlayer(self),
        }

        self.current_window = self.windows["edit"]
        self.navigate("edit")

        self.current_window.tkraise()


    def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=540.0, height=240.0)