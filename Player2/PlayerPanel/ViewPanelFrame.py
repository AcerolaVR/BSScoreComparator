# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from urllib.request import urlopen

import requests
import json
import api
import io
import os
from PIL import Image, ImageTk
import cloudscraper
import urllib
import datetime

# https://stackoverflow.com/questions/55943631/putting-svg-images-into-tkinter-frame

ASSETS_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(ASSETS_PATH, 'assets/frame0')

def getIcon(img_url):
    jpg_data = (
        cloudscraper.create_scraper(
            browser={"browser": "firefox", "platform": "windows", "mobile": False}
        )
            .get(img_url)
            .content
    )

    pil_image = Image.open(io.BytesIO(jpg_data))
    pil_image = pil_image.resize((128, 128))
    return ImageTk.PhotoImage(pil_image)


def getFlag(countryCode):
    pil_image = open('C:/Documents/GitHub/BSScoreComparator/build/assets/frame0/flags/' + countryCode + '.png')
    return ImageTk.PhotoImage(pil_image)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def view_player():
    ViewPlayer()

class ViewPlayer(Frame):
    def __init__(self, parent, playerHex, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.playerHex = playerHex

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
            201.0,
            64.0,
            anchor="nw",
            text= "#" + str(api.Player2.globalRank),
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            199.0,
            100.0,
            anchor="nw",
            text="#" + str(api.Player2.localRank),
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            150.0,
            4.0,
            anchor="nw",
            text=api.Player2.name,
            fill="#FFFFFF",
            font=("Inter", 48 * -1)
        )

        self.canvas.create_text(
            10.0,
            138.0,
            anchor="nw",
            text="Play Count",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            148.0,
            139.0,
            anchor="nw",
            text=api.Player2.rankedCount,
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            276.0,
            157.0,
            anchor="nw",
            text=str(api.Player2.pp) + "pp",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            10.0,
            172.0,
            anchor="nw",
            text="Accuracy",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            148.0,
            173.0,
            anchor="nw",
            text=str(api.Player2.rankedAcc)[0:5] + "%",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.image_globe = PhotoImage(
            file=relative_to_assets("globe.png"))
        self.canvas.create_image(
            172.0,
            76.0,
            image=self.image_globe)

        self.image_flag = PhotoImage(
            file=relative_to_assets("flags/" + api.Player2.country +".png"))
        self.canvas.create_image(
            170.0,
            112.0,
            image=self.image_flag)

        self.image_icon = getIcon(api.Player2.icon)
        image_PlayerIcon = self.canvas.create_image( 74.0, 74.0, image=self.image_icon )

        self.canvas.create_rectangle(
            10.0,
            204.0,
            417.0,
            224.0,
            # fill="#B71C1C",
            fill=self.playerHex,
            outline="")

        self.button_playerEditImg = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_playerEdit = Button(
            self.canvas,
            image=self.button_playerEditImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("edit"),
            cursor='hand2', activebackground="#343638",
            relief="flat"
        )

        self.button_playerEdit.place(
            x=426.0,
            y=177.0,
            width=110.0,
            height=50.0
        )

        self.canvas.create_rectangle(
            10.0,
            169.0,
            270.0,
            171.0,
            fill="#FFFFFF",
            outline="")