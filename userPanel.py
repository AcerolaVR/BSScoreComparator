#!/usr/bin/python3
from tkinter import END
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO

import main
import tkinter as tk
import tkinter.ttk as ttk

class UserWidget(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(UserWidget, self).__init__(master, **kw)
        frame1 = ttk.Frame(self)
        frame1.configure(
            borderwidth=10,
            height=200,
            relief="sunken",
            width=800)
        self.nameLabel = ttk.Label(frame1)
        self.nameLabel.configure(font="TkDefaultFont", text='Player')
        self.nameLabel.grid(column=1, row=0)

        self.countryLabel = ttk.Label(frame1)
        self.countryLabel.configure(text='Country')
        self.countryLabel.grid(column=1, row=1)

        self.ppLabel = ttk.Label(frame1)
        self.ppLabel.configure(text='Performance Points')
        self.ppLabel.grid(column=1, row=2)

        self.globalLabel = ttk.Label(frame1)
        self.globalLabel.configure(text='Global Rank')
        self.globalLabel.grid(column=1, row=3)

        self.localLabel = ttk.Label(frame1)
        self.localLabel.configure(text='Local Rank')
        self.localLabel.grid(column=1, row=4)

        self.rankedAccLabel = ttk.Label(frame1)
        self.rankedAccLabel.configure(text='Ranked Accuracy')
        self.rankedAccLabel.grid(column=1, row=5)

        self.rankedCountLabel = ttk.Label(frame1)
        self.rankedCountLabel.configure(text='Ranked Plays')
        self.rankedCountLabel.grid(column=1, row=6)

        self.userText = ttk.Entry(frame1)
        self.userText.configure(width=50)
        _text_ = 'Enter a Scoresaber URL, User ID, or username here\n'
        self.userText.delete("0", "end")
        self.userText.insert("0", _text_)
        self.userText.grid(column=2, row=0)

        self.countryText = ttk.Entry(frame1)
        self.countryText.grid(column=2, row=1)

        self.ppText = ttk.Entry(frame1)
        self.ppText.grid(column=2, row=2)

        self.globalText = ttk.Entry(frame1)
        self.globalText.grid(column=2, row=3)

        self.localText = ttk.Entry(frame1)
        self.localText.grid(column=2, row=4)

        self.rankedAccText = ttk.Entry(frame1)
        self.rankedAccText.grid(column=2, row=5)

        self.rankedCountText = ttk.Entry(frame1)
        self.rankedCountText.grid(column=2, row=6)

        frame1.grid(column=1, row=0)
        self.imgFrame = ttk.Frame(self)
        self.imgFrame.configure(height=160, width=160)
        self.imgFrame.grid(column=0, row=0)
        self.configure(height=200, width=200)

    def callback(self, event=None):
        pass

    # Define a function to clear the Entry Widget Content
    def clear_text(self):
        widget.userText.delete(0, END)

if __name__ == "__main__":
    User1 = main.loadUser(76561198002500746)
    root = tk.Tk()
    widget = UserWidget(root)
    # widget.pack_slaves(expand=True, fill="both")
    widget.clear_text()
    widget.userText.insert("0", User1.name)
    widget.countryText.insert("0", User1.country)
    widget.ppText.insert("0", User1.pp)
    widget.globalText.insert("0", User1.globalRank)
    widget.localText.insert("0", User1.localRank)
    widget.rankedAccText.insert("0", str(User1.rankedAcc) + "%")
    widget.rankedCountText.insert("0", User1.rankedCount)

    URL = "http://www.universeofsymbolism.com/images/ram-spirit-animal.jpg"
    u = urlopen(URL)
    raw_data = u.read()
    u.close()

    im = Image.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(im)

    img = main.getImage()

    # Create a Label Widget to display the text or Image
    label = ttk.Label(widget.imgFrame, image=img)
    label.pack()

    root.mainloop()
