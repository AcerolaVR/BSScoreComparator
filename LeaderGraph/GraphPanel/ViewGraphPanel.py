
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import api

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ViewGraph(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.canvas = Canvas(
            self,
            bg = "#343638",
            height = 580,
            width = 1113,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.canvas.create_text(
            50,
            50,
            anchor="nw",
            text="Placeholder",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

    #     draw graph here on canvas, width 1113, height 580

    def plotGraph(self):
        # plot graph

        # get songlist from current users
        self.left_songlist = api.Player1.songList
        self.right_songlist = api.Player2.songList

