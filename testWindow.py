# from pathlib import Path
# from tkinter import (
#     Toplevel,
#     Frame,
#     Canvas,
#     Button,
#     PhotoImage,
#     messagebox,
#     StringVar,
# )
#
# import requests
# import io
# import os
# from PIL import Image, ImageTk
# import cloudscraper
#
# from Player.Player import Player
#
# ASSETS_PATH = os.path.dirname(__file__)
# ASSETS_PATH = os.path.join(ASSETS_PATH, 'assets/frame0')
#
#
# def mainWindow():
#     MainWindow()
#
#
# class MainWindow(Toplevel):
#     global user1
#     global user2
#
#     def __init__(self, *args, **kwargs):
#         Toplevel.__init__(self, *args, **kwargs)
#
#         self.title("Beat Saber Score Comparator")
#
#         self.geometry("540x240")
#         self.configure(bg="#5E95FF")
#
#         self.canvas = Canvas(
#             self,
#             bg="#5E95FF",
#             height=240,
#             width=540,
#             bd=0,
#             highlightthickness=0,
#             relief="ridge",
#         )
#
#         self.canvas.place(x=0, y=0)
#
#         # Loop through windows and place them
#         self.windows = {
#             "player": Player(self),
#         }
#
#         self.current_window.place(x=215, y=72, width=540.0, height=240.0)
#
#         self.current_window.tkraise()
#         self.resizable(False, False)
#         self.mainloop()
