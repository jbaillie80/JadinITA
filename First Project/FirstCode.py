'''
Created on Nov 18, 2021

@author: jadin
'''
import random

import os
clear = lambda: os.system('cls')
clear()

def test():
    Correct = 0
    Q1 = input("What is the power house of the cell? A) mitochondria B) nucleous C) ribosome")
    if (Q1 == "A" or Q1 == "a"):
        print("Correct")
        Correct = Correct+1
    elif (Q1 == "B" or Q1 == "b"):
        print("Incorrect")
    elif (Q1 == "C" or Q1 == "c"):
        print("Incorrect")
    else:
        print("Please type, A, B, or C")
    
    Q2 = input("How many states comprise the United States? A) 13 B) 45 C) 50")
    if (Q2 == "A" or Q2 == "a"):
        print("Incorrect")
    elif (Q2 == "B" or Q2 == "b"):
        print("Incorrect")
    elif (Q2 == "C" or Q2 == "c"):
        print("Correct")
        Correct = Correct+1
    else:
        print("Please type, A, B, or C")
        
    Q3 = input("In English, a person, place or thing is called: A) verb B) adjective C) noun")
    if (Q3 == "A" or Q3 == "a"):
        print("Incorrect")
    elif (Q3 == "B" or Q3 == "b"):
        print("Incorrect")
    elif (Q3 == "C" or Q3 == "c"):
        print("Correct")
        Correct = Correct+1
    else:
        print("Please type, A, B, or C")
        
    print("You got " + str(Correct) + " answers right")
    return

def RockPaperScissors ():
    
    comp = random.choice(["Rock", "Paper", "Scissors"])
    x = 0
    UserScore = 0
    CompScore = 0
    while x <= 6:
        UserInp = input("Rock... Paper... Scissors... GO! ")
        comp = random.choice(["Rock", "Paper", "Scissors"])
        clear()
        if x == 5:
            print("You have " + str(UserScore) + " points")
            print("They have " + str(CompScore) + " points")
            if UserScore > CompScore:
                print("You Win!")
                x = x + 1
            elif UserScore < CompScore:
                print("You Lose!")
                x = x + 1
            else:
                print("Tie!")
                x = x + 1
        elif UserInp == "ROCK":
            clear()
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

