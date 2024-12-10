import game_data, art
import random, os

def LooserScreen():
    os.system('cls')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")

def ContinueGame(vsList: list):
    print(art.logo)
    print(f"You're right! Current score: {score}.")
    print(f"Compare A: {vsList[0][0]}, a {vsList[0][2]}, from {vsList[0][3]}.")
    print(art.vs)
    print(f"Against B: {vsList[1][0]}, a {vsList[1][2]}, from {vsList[1][3]}.")
    global guess 
    guess = input("Who has more followers? Type 'A' or 'B': ")

def PullContestant() -> list:
    gameList = game_data.data
    random.shuffle(gameList)
    tempDic1 = gameList[0]
    tempDic2 = gameList[1]
    nameA = tempDic1["name"]
    nameB = tempDic2["name"]
    followerA = tempDic1["follower_count"]
    followerB = tempDic2["follower_count"]
    descriptionA = tempDic1["description"]
    descriptionB = tempDic2["description"]
    countryA = tempDic1["country"]
    countryB = tempDic2["country"]

    return [[nameA, followerA, descriptionA, countryA], [nameB, followerB, descriptionB, countryB]]

score = 0
print(art.logo) 
vsList = PullContestant()
print(f"Compare A: {vsList[0][0]}, a {vsList[0][2]}, from {vsList[0][3]}.")
print(art.vs)
print(f"Against B: {vsList[1][0]}, a {vsList[1][2]}, from {vsList[1][3]}.")
guess = input("Who has more followers? Type 'A' or 'B': ")
while True:
    if guess == "A" and vsList[0][1] > vsList[1][1]:
        score += 1
        tempList = vsList[0]
        vsList = PullContestant()
        vsList[0] = tempList
        ContinueGame(vsList)
    elif guess == "B" and vsList[1][1] > vsList[0][1]:
        score += 1
        tempList = vsList[1]
        vsList = PullContestant()
        vsList[0] = tempList
        ContinueGame(vsList)
    else:
        LooserScreen()
        break





    

