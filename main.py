# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import os
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage

import api
from Player.PlayerFrame import PlayerWidget
from LeaderGraph.LeaderGraphFrame import LeaderGraphWidget

ASSETS_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(ASSETS_PATH, 'assets/frame0')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window = Tk()

window.geometry("1220x1024")
window.configure(bg="#6F6F6F")

# Player1 = api.loadUser('https://scoresaber.com/u/76561198002500746')
# Player2 = api.loadUser('76561198002500746')

api.Player1 = api.loadUser('76561198988695829')
api.Player2 = api.loadUser('76561198333869741')

PlayerFrame1 = PlayerWidget(api.Player1, window, "#B71C1C", bg="#343638", width=540, height=240)
PlayerFrame2 = PlayerWidget(api.Player2, window, "#003BFF", bg="#343638", width=540, height=240)
LeaderGraph1 = LeaderGraphWidget(window, bg="#343638", width=1113, height=680)

canvas = Canvas(
    window,
    bg="#6F6F6F",
    height=1024,
    width=1220,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# place and raise the player frames on the main window
PlayerFrame1.place(x=77, y=11, width=540.0, height=240.0)
PlayerFrame2.place(x=650, y=11, width=540.0, height=240.0)
LeaderGraph1.place(x=77, y=309, width=1113.0, height=680.0)

PlayerFrame1.tkraise()
PlayerFrame2.tkraise()
LeaderGraph1.tkraise()
LeaderGraph1.left_sortByPP()

canvas.create_rectangle(
    650.0,
    11.0,
    1190.0,
    251.0,
    fill="#343638",
    outline="")

canvas.create_rectangle(
    77.0,
    309.0,
    1190.0,
    989.0,
    fill="#343638",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: LeaderGraph1.navigate('leaderboard'),
    relief="flat"
)
button_1.place(
    x=16.0,
    y=309.0,
    width=45.0,
    height=45.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: LeaderGraph1.navigate('graph'),
    relief="flat"
)
button_2.place(
    x=16.0,
    y=369.0,
    width=45.0,
    height=45.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: LeaderGraph1.left_sortByUnplayed(),
    relief="flat"
)
button_3.place(
    x=489.0,
    y=265.0,
    width=128.0,
    height=32.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: LeaderGraph1.left_sortByRecent(),
    relief="flat"
)
button_4.place(
    x=347.0,
    y=265.0,
    width=128.0,
    height=32.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: LeaderGraph1.left_sortByPP(),
    relief="flat"
)
button_5.place(
    x=205.0,
    y=265.0,
    width=128.0,
    height=32.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: LeaderGraph1.right_sortByUnplayed(),
    relief="flat"
)
button_6.place(
    x=1062.0,
    y=261.0,
    width=128.0,
    height=32.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: LeaderGraph1.right_sortByRecent(),
    relief="flat"
)
button_7.place(
    x=920.0,
    y=261.0,
    width=128.0,
    height=32.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: LeaderGraph1.right_sortByPP(),
    relief="flat"
)
button_8.place(
    x=778.0,
    y=261.0,
    width=128.0,
    height=32.0
)

canvas.create_rectangle(
    77.0,
    11.0,
    617.0,
    251.0,
    fill="#000000",
    outline="")

window.resizable(False, False)
window.mainloop()
