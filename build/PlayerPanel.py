# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from urllib.request import urlopen

import PIL.Image
import requests
import json
import io
import os
from PIL import Image, ImageTk
import PySimpleGUI as sg
import cloudscraper
import urllib
import datetime
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

# https://stackoverflow.com/questions/55943631/putting-svg-images-into-tkinter-frame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("C:/Documents/GitHub/BSScoreComparator/build/assets/frame0")

class User:
    def __init__(self, name, country, pp, globalRank, localRank, rankedAcc, rankedCount, icon):
        self.name = name
        self.country = country
        self.pp = pp
        self.globalRank = globalRank
        self.localRank = localRank
        self.rankedAcc = rankedAcc
        self.rankedCount = rankedCount
        self.icon = icon


def loadUser(userID):
    user_response = requests.get('https://scoresaber.com/api/player/' + str(userID) + '/full')

    newUser = User(user_response.json()["name"],
                   user_response.json()["country"],
                   user_response.json()["pp"],
                   user_response.json()["rank"],
                   user_response.json()["countryRank"],
                   user_response.json()['scoreStats']["averageRankedAccuracy"],
                   user_response.json()['scoreStats']["rankedPlayCount"],
                   user_response.json()['profilePicture'])

    return newUser


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


User1 = loadUser(76561198002500746)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("540x240")
window.configure(bg="#343638")

canvas = Canvas(
    window,
    bg="#343638",
    height=240,
    width=540,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    201.0,
    64.0,
    anchor="nw",
    text="#1,218",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    199.0,
    100.0,
    anchor="nw",
    text="#525",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    150.0,
    4.0,
    anchor="nw",
    text=User1.name,
    fill="#FFFFFF",
    font=("Inter", 48 * -1)
)

canvas.create_text(
    10.0,
    138.0,
    anchor="nw",
    text="Ranked Play Count",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    260.0,
    139.0,
    anchor="nw",
    text=User1.rankedCount,
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    10.0,
    172.0,
    anchor="nw",
    text="Ranked Accuracy",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    260.0,
    173.0,
    anchor="nw",
    text=str(User1.rankedAcc)[0:5] + "%",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    151.0,
    59.0,
    189.0,
    97.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    150.0,
    99.0,
    189.0,
    128.0,
    fill="#000000",
    outline="")

# image_image_1 = PhotoImage(
#     file=relative_to_assets("image_1.png"))
image_image_1 = getIcon(User1.icon)
image_1 = canvas.create_image(
    74.0,
    74.0,
    image=image_image_1
)

canvas.create_rectangle(
    10.0,
    204.0,
    417.0,
    224.0,
    fill="#B71C1C",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=426.0,
    y=177.0,
    width=110.0,
    height=50.0
)

canvas.create_rectangle(
    9.0,
    169.0,
    375.0,
    171.0,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()
