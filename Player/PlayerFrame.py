import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from tkinter import Tk, Canvas, Listbox, Entry, Text, Button, PhotoImage, END, Frame

import requests
import re
from urlextract import URLExtract

from PlayerPanel.ViewPanelFrame import ViewPlayer
from EditPanel.EditPanelFrame import EditPlayer
from RecentPanel.RecentPanelFrame import RecentPlayer

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


def loadUser(userInput):
    # detect url
    # scrub non-numeric text from
    userInput = re.sub('[^0-9]', '', userInput)

    user_response = requests.get('https://scoresaber.com/api/player/' + str(userInput) + '/full')

    # detect that a valid user was returned with the response
    if (user_response.status_code == 404):
        print('http error caught')

    newUser = User(user_response.json()["name"],
                   user_response.json()["country"],
                   user_response.json()["pp"],
                   user_response.json()["rank"],
                   user_response.json()["countryRank"],
                   user_response.json()['scoreStats']["averageRankedAccuracy"],
                   user_response.json()['scoreStats']["rankedPlayCount"],
                   user_response.json()['profilePicture'])

    return newUser

class PlayerWidget(Frame):
    def __init__(self, player, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.player = player

        self.configure(bg="#343638")

        # Loop through windows and place them
        self.windows = {
            "view": ViewPlayer(self),
            "edit": EditPlayer(self),
            "recent": RecentPlayer(self),
        }

        self.current_window = self.windows["edit"]
        self.navigate("edit")

        self.current_window.tkraise()

    def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=540.0, height=240.0)

    @staticmethod
    def loadUser(userInput):
        # detect url

        #scrub non-numeric text from
        userInput = re.sub('[^0-9]', '', userInput)

        user_response = requests.get('https://scoresaber.com/api/player/' + str(userInput) + '/full')

        #detect that a valid user was returned with the response
        if(user_response.status_code == 404):
            print('http error caught')


        newUser = User(user_response.json()["name"],
                       user_response.json()["country"],
                       user_response.json()["pp"],
                       user_response.json()["rank"],
                       user_response.json()["countryRank"],
                       user_response.json()['scoreStats']["averageRankedAccuracy"],
                       user_response.json()['scoreStats']["rankedPlayCount"],
                       user_response.json()['profilePicture'])

        return newUser

if __name__ == "__main__":
    test = Tk()

    # User1 = loadUser(76561198002500746)  # Acerola
    # Player1 = loadUser(76561198404774259) #SilentBang
    # Player2 = loadUser(76561198333869741) #Cerret

    # Player1 = loadUser('https://scoresaber.com/u/761198002500746')
    Player1 = loadUser('https://scoresaber.com/u/76561198002500746')
    Player2 = loadUser('76561198002500746')

    test.geometry("1100x300")
    test.configure(bg="#343638")

    PlayerFrame1 = PlayerWidget(Player1, test, bg="#343638", width=540, height=240)
    PlayerFrame1.place(x=0, y=0, width=540.0, height=240.0)

    PlayerFrame2 = PlayerWidget(Player2, test, bg="#343638", width=540, height=240)
    PlayerFrame2.place(x=540, y=0, width=540.0, height=240.0)

    test.resizable(False, False)
    test.mainloop()
