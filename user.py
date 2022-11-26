import requests
import validators
import re
import tkinter as tk
import traceback
import tkinter.messagebox
import json

class User:
    def __init__(self, id, name, country, pp, globalRank, localRank, rankedAcc, rankedCount, icon):
        self.id = id
        self.name = name
        self.country = country
        self.pp = pp
        self.globalRank = globalRank
        self.localRank = localRank
        self.rankedAcc = rankedAcc
        self.rankedCount = rankedCount
        self.icon = icon


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
                   user_response.json()['profilePicture'])

    return newUser


# function to add to JSON
def write_json(new_data, filename='recentUsers.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["recent_players"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


def report_callback_exception(self, *args):
    err = traceback.format_exception(*args)
    tkinter.messagebox.showerror('Exception', err)
