import tkinter
import requests
import json
import io
import os
from PIL import Image, ImageTk
import PySimpleGUI as sg
import cloudscraper
import urllib

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
  def __init__(self, name, artist, mapper, score, accuracy, pp, img, fullCombo, maxCombo, badCuts, misses):
    self.name = name
    self.artist = artist
    self.mapper = mapper
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
        print(play_response.json()['playerScores'][x]['leaderboard']['songName'])
        print(play_response.json()['playerScores'][x]['leaderboard']['songAuthorName'])
        print(play_response.json()['playerScores'][x]['leaderboard']['levelAuthorName'])

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    User1 = loadUser(76561198002500746)
    SongList = LoadUserSongs(76561198002500746, 100)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
