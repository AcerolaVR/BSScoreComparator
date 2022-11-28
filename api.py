import tkinter
from urllib.request import urlopen

import requests
import json
import io
import os
from PIL import Image, ImageTk
import PySimpleGUI as sg
import cloudscraper
import urllib
import datetime
import validators
import re

sg.theme('DarkAmber')


def getIcon(img_url, w=128, h=128):
    jpg_data = (
        cloudscraper.create_scraper(
            browser={"browser": "firefox", "platform": "windows", "mobile": False}
        )
            .get(img_url)
            .content
    )

    pil_image = Image.open(io.BytesIO(jpg_data))
    pil_image = pil_image.resize((w, h))
    return ImageTk.PhotoImage(pil_image)


class User:
    def __init__(self, id, name, country, pp, globalRank, localRank, rankedAcc, rankedCount, icon, songList):
        self.id = id
        self.name = name
        self.country = country
        self.pp = pp
        self.globalRank = globalRank
        self.localRank = localRank
        self.rankedAcc = rankedAcc
        self.rankedCount = rankedCount
        self.icon = icon
        self.songList = songList


class Song:
    def __init__(self, id, name, artist, mapper, timeSet, stars, score, accuracy, pp, img, fullCombo, maxCombo, badCuts,
                 misses):
        self.id = id
        self.name = name
        self.artist = artist
        self.mapper = mapper
        self.timeSet = datetime.datetime.strptime(timeSet, "%Y-%m-%dT%H:%M:%S.000Z")
        self.stars = stars
        self.score = score
        self.accuracy = accuracy
        self.pp = pp
        self.image = img
        self.fullCombo = fullCombo
        self.maxCombo = maxCombo
        self.badCuts = badCuts
        self.misses = misses


@staticmethod
def loadUser(userInput):
    errorValues = ["We couldn't find a user with the id",
                   "We couldn't find a user with the given url",
                   "We couldn't find a user with the given username"]

    # handle ID inputs
    if userInput.isdigit():
        userID = userInput
        error = errorValues[0]
    # handle URL inputs
    elif validators.url(userInput):
        # scrub non-numeric text from url
        userID = re.sub('[^0-9]', '', userInput)
        error = errorValues[1]
    # handle string inputs, which would probably be a username
    else:
        username = requests.get('https://scoresaber.com/api/players?search=' + str(userInput))
        print(username.json())
        error = errorValues[2]
        # detect that a valid user was returned with the response
        if (username.status_code == 404):
            print('http error caught')
            print(username.json()['errorMessage'])
            raise Exception(error)
        userID = username.json()['players'][0]["id"]

    user_response = requests.get('https://scoresaber.com/api/player/' + str(userID) + '/full')

    # detect that a valid user was returned with the response
    if (user_response.status_code == 404):
        raise Exception(error)

    write_json(user_response.json())

    newUser = User(user_response.json()["id"],
                   user_response.json()["name"],
                   user_response.json()["country"],
                   user_response.json()["pp"],
                   user_response.json()["rank"],
                   user_response.json()["countryRank"],
                   user_response.json()['scoreStats']["averageRankedAccuracy"],
                   user_response.json()['scoreStats']["rankedPlayCount"],
                   user_response.json()['profilePicture'],
                   LoadUserSongs(userID, 20))

    return newUser


# function to add to JSON
def write_json(new_data, filename='recentUsers.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # if new_data['id'] in file_data.values():
        print(new_data['id'])
        print(str(file_data['recent_players']))

        # if new_data['id'] in file_data['recent_players']:
        if str(file_data['recent_players']).__contains__(str(new_data['id'])):
            print('user already exists')
            pass
        else:
            print('new user found, adding to recent user list')
            file_data["recent_players"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


def report_callback_exception(self, *args):
    err = traceback.format_exception(*args)
    tkinter.messagebox.showerror('Exception', err)


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
                             100 * (play_response.json()['playerScores'][x]['score']['baseScore'] /
                                    play_response.json()['playerScores'][x]['leaderboard']['maxScore']),
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
    u = urlopen(img_url)
    raw_data = u.read()
    u.close()

    im = Image.open(io.BytesIO(raw_data))
    return ImageTk.PhotoImage(im)


def sortByPP(songs):
    return sorted(songs, key=lambda x: x.pp, reverse=True)


def sortByRecent(songs):
    return sorted(songs, key=lambda x: x.timeSet, reverse=True)


def sortByUnplayed(songs1, songs2):
    def check(x1, songs):
        for x2 in songs:
            if x1.id == x2.id:
                return True
        return False

    return [x for x in songs1 if not check(x, songs2)]


def getCorrespondingList(songs1, songs2):
    def getSong(x1, songs):
        for x2 in songs:
            if x1.id == x2.id:
                return x2
        return None

    ret = []
    for x in songs1:
        ret.append(getSong(x, songs2))
    return ret


def SortTest(SongList):
    import random
    random.shuffle(SongList)
    SongList = sortByPP(SongList)
    SongList = sortByRecent(SongList)
    SongList2 = SongList.copy()
    print(SongList[10])
    del SongList2[10]
    print(sortByUnplayed(SongList, SongList2))


global Player1
global Player2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    User1 = loadUser(76561198002500746)
    SongList = LoadUserSongs(76561198002500746, 100)
    print(SongList)
    SortTest(SongList.copy())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
