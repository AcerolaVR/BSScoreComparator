import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from tkinter import Tk, Canvas, Listbox, Entry, Text, Button, PhotoImage, END, Frame

import requests
import re
from urlextract import URLExtract

from .PlayerPanel.ViewPanelFrame import ViewPlayer
from .EditPanel.EditPanelFrame import EditPlayer
from .RecentPanel.RecentPanelFrame import RecentPlayer

import user

class PlayerWidget(Frame):
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
            "recent": RecentPlayer(self),
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

# if __name__ == "__main__":
#     test = Tk()
#
#     # User1 = loadUser(76561198002500746)  # Acerola
#     # Player1 = loadUser(76561198404774259) #SilentBang
#     # Player2 = loadUser(76561198333869741) #Cerret
#
#     # Player1 = loadUser('https://scoresaber.com/u/761198002500746')
#     Player1 = user.loadUser('https://scoresaber.com/u/76561198002500746')
#     Player2 = user.loadUser('76561198002500746')
#
#     test.geometry("1100x300")
#     test.configure(bg="#343638")
#
#     PlayerFrame1 = PlayerWidget(Player1, test, bg="#343638", width=540, height=240)
#     PlayerFrame1.place(x=0, y=0, width=540.0, height=240.0)
#
#     PlayerFrame2 = PlayerWidget(Player2, test, bg="#343638", width=540, height=240)
#     PlayerFrame2.place(x=540, y=0, width=540.0, height=240.0)
#
#     test.resizable(False, False)
#     test.mainloop()
