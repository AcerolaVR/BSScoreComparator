# from plot_graph import plot_graph
import tkinter
import requests
import json
import io
import os
from PIL import Image, ImageTk
import PySimpleGUI as sg
import cloudscraper
import urllib
import datetime
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

sg.theme('DarkAmber')


class User:
    def __init__(self, name, country, pp, globalRank, localRank, rankedAcc, rankedCount):
        self.name = name
        self.country = country
        self.pp = pp
        self.globalRank = globalRank
        self.localRank = localRank
        self.rankedAcc = rankedAcc
        self.rankedCount = rankedCount


class Song:
    def __init__(self, id, name, artist, mapper, timeSet, stars, score, accuracy, pp, img, fullCombo, maxCombo, badCuts, misses):
        self.id = id
        self.name = name
        self.artist = artist
        self.mapper = mapper
        self.timeSet = timeSet
        self.stars = stars
        self.score = score
        self.accuracy = accuracy
        self.pp = pp
        self.image = img
        self.fullCombo = fullCombo
        self.maxCombo = maxCombo
        self.badCuts = badCuts
        self.misses = misses


def loadUser(userID):
    user_response = requests.get('https://scoresaber.com/api/player/' + str(userID) + '/full')

    newUser = User(user_response.json()["name"],
                   user_response.json()["country"],
                   user_response.json()["pp"],
                   user_response.json()["rank"],
                   user_response.json()["countryRank"],
                   user_response.json()['scoreStats']["averageRankedAccuracy"],
                   user_response.json()['scoreStats']["rankedPlayCount"])

    return newUser


def LoadUserSongs(userID, len):
    # play_response = requests.get('https://scoresaber.com/api/player/' + str(userID) + '/scores?limit=' + str(99) + 'sort=top&withMetadata=true')
    play_response = requests.get(
        'https://scoresaber.com/api/player/' + str(userID) + '/scores?limit=100&sort=top&withMetadata=true')
    songList = []

    for x in range(len):
        songList.append(Song(play_response.json()['playerScores'][x]['leaderboard']['id'],
                             play_response.json()['playerScores'][x]['leaderboard']['songName'],
                             play_response.json()['playerScores'][x]['leaderboard']['songAuthorName'],
                             play_response.json()['playerScores'][x]['leaderboard']['levelAuthorName'],
                             play_response.json()['playerScores'][x]['score']['timeSet'],
                             play_response.json()['playerScores'][x]['leaderboard']['stars'],
                             play_response.json()['playerScores'][x]['score']['baseScore'],
                             100 * (play_response.json()['playerScores'][x]['score']['baseScore'] / play_response.json()['playerScores'][x]['leaderboard']['maxScore']),
                             play_response.json()['playerScores'][x]['score']['pp'],
                             play_response.json()['playerScores'][x]['leaderboard']['coverImage'],
                             play_response.json()['playerScores'][x]['score']['fullCombo'],
                             play_response.json()['playerScores'][x]['score']['maxCombo'],
                             play_response.json()['playerScores'][x]['score']['badCuts'],
                             play_response.json()['playerScores'][x]['score']['missedNotes']
                             )
                        )

    return songList


def getImage(img_url):
    jpg_data = (
        cloudscraper.create_scraper(
            browser={"browser": "firefox", "platform": "windows", "mobile": False}
        )
            .get(img_url)
            .content
    )

    pil_image = Image.open(io.BytesIO(jpg_data))
    png_bio = io.BytesIO()
    pil_image.save(png_bio, format="PNG")
    return png_bio.getvalue()

def sortByPP(songs):
    return sorted(songs, key=lambda x: x.pp, reverse=True) 

def sortByRecent(songs):
    return sorted(songs, key=lambda x: datetime.datetime.strptime(x.timeSet, "%Y-%m-%dT%H:%M:%S.000Z")) 

def sortByUnplayed(songs1, songs2):
    def check(x1, songs):
        for x2 in songs:
            if x1.id == x2.id:
                return True
        return False
    return [x for x in songs1 if not check(x, songs2)]

def SortTest(SongList):
    import random
    random.shuffle(SongList)
    SongList = sortByPP(SongList)
    SongList = sortByRecent(SongList)
    SongList2 = SongList.copy()
    print(SongList[10])
    del SongList2[10]
    print(sortByUnplayed(SongList, SongList2))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # User1 = loadUser(76561198002500746)
    SongList = LoadUserSongs(76561198002500746, 100)
    unweightedPP = []
    for i in range(100):
        unweightedPP.append(SongList[i].pp)
    # print(unweightedPP)
    # SortTest(SongList.copy())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# plot function is created for 
# plotting the graph in 
# tkinter window
def plot_graph(y):
  
    # the figure that will contain the plot
    fig = Figure(figsize=(5,5), dpi=100)

  
    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.grid()
    plot1.set_xlabel('Play counts')
    plot1.set_ylabel('Unweighted PP')
  
    # plotting the graph
    plot1.plot(y)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

  
# the main Tkinter window
window = tk.Tk()
  
# setting the title 
window.title('UnweightedPP vs play count')
  
# dimensions of the main window
window.geometry("500x500")
  
# button that displays the plot
plot_button = tk.Button(master = window, 
                     command = plot_graph(y = unweightedPP),
                     height = 2, 
                     width = 10,
                     text = "Plot")
  
# place the button 
# in main window
plot_button.pack()
  
# run the gui
window.mainloop()
