# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import webbrowser
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, OptionMenu, StringVar, messagebox, END
import traceback

import requests
import io
import os
import api
import re
import json
from PIL import Image, ImageTk
import cloudscraper

ASSETS_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(ASSETS_PATH, 'assets/frame0')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class EditPlayer(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.entryData = 0

        self.configure(bg="#343638")

        self.canvas = Canvas(
            self,
            bg="#343638",
            height=240,
            width=540,
            bd=0,
            highlightthickness=0,
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_text(
            10.0,
            0.0,
            anchor="nw",
            text="Enter Player Here",
            fill="#FFFFFF",
            font=("Inter", 36 * -1)
        )

        self.canvas.create_text(
            10.0,
            80.0,
            anchor="nw",
            text="Accepts Usernames, Scoresaber URLs, and Scoresaber IDs",
            fill="#A2A4A6",
            font=("Inter", 16 * -1)
        )

        self.exceptionText = self.canvas.create_text(
            10.0,
            166.0,
            anchor="nw",
            fill="#FF0000",
            font=("Inter", 14 * -1)
        )

        variable = StringVar(self)
        lst = []

        with open('recentUsers.json', 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)

            for recentUser in file_data['recent_players']:
                lst.append(str(recentUser['name']) + ' | ' + str(recentUser['id']))

        self.recentListbox = OptionMenu(
            self.canvas,
            variable,
            *lst,
            command=self.recentFunc,
        )

        self.recentListbox.place(
            x=10.0,
            y=100.0,
            height=30,
            width=520,
        )

        self.button_scoresaber_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_scoresaber = Button(
            self.canvas,
            image=self.button_scoresaber_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: webbrowser.open('https://scoresaber.com/rankings'),
            cursor='hand2', activebackground="#343638",
            relief="flat"
        )
        self.button_scoresaber.place(
            x=10.0,
            y=204.0,
            width=190.0,
            height=25.0
        )

        self.button_view_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_view = Button(
            self.canvas,
            image=self.button_view_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.LoadPlayerView(self.entry_1.get()),
            cursor='hand2', activebackground="#343638",
            relief="flat"
        )
        self.button_view.place(
            x=378.0,
            y=199.0,
            width=152.0,
            height=30.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            270.0,
            62.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            # textvariable=self.entryData,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 16 * -1),
        )
        self.entry_1.place(
            x=10.0,
            y=46.0,
            width=520.0,
            height=30.0
        )

    def recentFunc(self, value):
        value = value.split(' | ', 1)[1]
        userID = re.sub('[^0-9]', '', str(value))
        self.LoadPlayerView(userID)

    def displayException(self, exception):
        self.exceptionText = self.canvas.create_text(
            10.0,
            166.0,
            anchor="nw",
            text=exception,
            fill="#FF0000",
            font=("Inter", 14 * -1)
        )

    def deleteException(self):
        self.canvas.delete(self.exceptionText)

    def LoadPlayerView(self, entry):
        self.deleteException()
        print(entry)
        # print(self.entry_1)
        try:
            api.Player1 = api.loadUser(entry)
            print(self.parent.player.name)
            # print(api.Player1.name)
            # print(api.Player2.name)
            self.parent.windows["view"].destroy()
            self.parent.windows["view"].__init__(self.parent, self.parent.playerHex)
            self.parent.navigate("view")
        except Exception as e:
            self.displayException(e)
