import random
import os
os.system('cls')

def RockPaperScissors ():
    for i in range(10):
        print("_")
    comp = random.choice(["Rock", "Paper", "Scissors"])
    x = 0
    UserScore = 0
    CompScore = 0
    while x < 6:
        if x == 5:
            print("You have " + str(UserScore) + " points")
            print("They have " + str(CompScore) + " points")
            if UserScore > CompScore:
                print("You Win!")
                x = x + 1
                break
            elif UserScore < CompScore:
                print("You Lose!")
                x = x + 1
                break
            else:
                print("Tie!")
                x = x + 1
                break
        UserInp = input("Rock... Paper... Scissors... GO! ")
        UserInp = UserInp.upper()
        comp = random.choice(["Rock", "Paper", "Scissors"])
        for i in range(10):
            print("_")
        if UserInp == "ROCK":
            if comp == "Rock":
                x = x + 1
                print("Your opponent chose " + comp + "... Tie!")
            elif comp == "Paper":
                x = x + 1
                CompScore = CompScore + 1
                print("Your opponent chose " + comp + "... They got a point!")
            else:
                x = x + 1
                UserScore = UserScore + 1
                print("Your opponent chose " + comp + "... You got a point!")
        elif UserInp == "PAPER":
            if comp == "Rock":
                x = x + 1
                UserScore = UserScore + 1
                print("Your opponent chose " + comp + "... You got a point!")
            elif comp == "Paper":
                x = x + 1
                print("Your opponent chose " + comp + "... Tie!")
            else:
                x = x + 1
                CompScore = CompScore + 1
                print("Your opponent chose " + comp + "... They got a point!")
        elif UserInp == "SCISSORS":
            if comp == "Rock":
                x = x + 1
                CompScore = CompScore + 1
                print("Your opponent chose " + comp + "... They got a point!")
            elif comp == "Paper":
                x = x + 1
                UserScore = UserScore + 1
                print("Your opponent chose " + comp + "... You got a point!")
            else:
                x = x + 1
                print("Your opponent chose " + comp + "... Tie!")
        elif UserInp == "STOP":
            break
        elif UserInp == "SCORE":
            print("You have " + str(UserScore) + " points")
            print("They have " + str(CompScore) + " points")
        else:
            print("Invalid Input")

RockPaperScissors()