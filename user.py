import requests
import re


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
    # detect url

    # scrub non-numeric text from
    userInput = re.sub('[^0-9]', '', userInput)

    user_response = requests.get('https://scoresaber.com/api/player/' + str(userInput) + '/full')

    # detect that a valid user was returned with the response
    if (user_response.status_code == 404):
        print('http error caught')

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
