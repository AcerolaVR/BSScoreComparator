try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import Tk, Canvas, Listbox, Entry, Text, Button, PhotoImage, END, Frame

except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from EditPanel.EditPanelFrame import EditPlayer
from PlayerPanel.PlayerPanelFrame import ViewPlayer
from RecentPanel.RecentPanelFrame import RecentPlayer

class PlayerWidget(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.canvas = Canvas(
            self,
            bg="#343638",
            height=240,
            width=540,
            bd=0,
            highlightthickness=0,
        )

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (EditPlayer, ViewPlayer, RecentPlayer):
        # for F in (StartPage, RecentPlayer):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("EditPlayer")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = PlayerWidget()
    app.geometry('540x240')
    # app.resizable(False, False)
    app.mainloop()