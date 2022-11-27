import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from tkinter import Tk, Canvas, Listbox, Entry, Text, Button, PhotoImage, END, Frame

import requests
import re
from urlextract import URLExtract

from .SongPanel.ViewSongPanel import ViewSong
from .GraphPanel.ViewGraphPanel import ViewGraph

import user

class LeaderGraphWidget(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # self.player = player

        self.configure(bg="#343638")

        # Loop through windows and place them
        self.windows = {
            "leaderboard": ViewSong(self),
            "graph": ViewGraph(self),
        }

        self.current_window = self.windows["leaderboard"]
        self.navigate("leaderboard")

        self.current_window.tkraise()


    def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=1113.0, height=680.0)