
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from urllib.request import urlopen

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("C:\Documents\GitHub\BSScoreComparator\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("540x240")
window.configure(bg = "#343638")


canvas = Canvas(
    window,
    bg = "#343638",
    height = 240,
    width = 540,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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
    text="Acerola",
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
    text="Plays",
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
    text="Accuracy",
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

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
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
