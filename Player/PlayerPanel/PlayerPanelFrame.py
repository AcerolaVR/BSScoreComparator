# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from urllib.request import urlopen

import requests
import json
import io
import os
from PIL import Image, ImageTk
import cloudscraper
import urllib
import datetime

# https://stackoverflow.com/questions/55943631/putting-svg-images-into-tkinter-frame

ASSETS_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(ASSETS_PATH, 'assets/frame0')

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


def getFlag(countryCode):
    pil_image = open('C:/Documents/GitHub/BSScoreComparator/build/assets/frame0/flags/' + countryCode + '.png')
    return ImageTk.PhotoImage(pil_image)


User1 = loadUser(76561198002500746) #Acerola
# User1 = loadUser(76561198404774259) #SilentBang
# User1 = loadUser(76561198333869741) #Cerret



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def view_player():
    ViewPlayer()

class ViewPlayer(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

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
            text= "#" + str(User1.globalRank),
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            199.0,
            100.0,
            anchor="nw",
            text="#" + str(User1.localRank),
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            150.0,
            4.0,
            anchor="nw",
            text=User1.name,
            fill="#FFFFFF",
            font=("Inter", 48 * -1)
        )

        self.canvas.create_text(
            10.0,
            138.0,
            anchor="nw",
            text="Ranked Play Count",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            260.0,
            139.0,
            anchor="nw",
            text=User1.rankedCount,
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            10.0,
            172.0,
            anchor="nw",
            text="Ranked Accuracy",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            260.0,
            173.0,
            anchor="nw",
            text=str(User1.rankedAcc)[0:5] + "%",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        image_globe = PhotoImage(
            file=relative_to_assets("globe.png"))
        self.canvas.create_image(
            172.0,
            76.0,
            image=image_globe)

        image_flag = PhotoImage(
            file=relative_to_assets("flags/" + User1.country +".png"))
        self.canvas.create_image(
            170.0,
            112.0,
            image=image_flag)

        image_icon = getIcon(User1.icon)
        image_PlayerIcon = self.canvas.create_image(
            74.0,
            74.0,
            image=image_icon
        )

        self.canvas.create_rectangle(
            10.0,
            204.0,
            417.0,
            224.0,
            fill="#B71C1C",
            outline="")

        button_playerEditImg = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_playerEdit = Button(
            image=button_playerEditImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_playerEdit.place(
            x=426.0,
            y=177.0,
            width=110.0,
            height=50.0
        )

        self.canvas.create_rectangle(
            9.0,
            169.0,
            375.0,
            171.0,
            fill="#FFFFFF",
            outline="")