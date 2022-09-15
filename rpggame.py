import random
import time

def displayIntro():
    print("It is the end of a decade of fighting the space cowboy war.")
    print("You come to crossroads on your trip home, the first path leads home.")
    print("Where you will be handsomely rewarded for a job well done.")
    print("The second leads through a gamma ray burst that will disintegrate you.")
    print("The third path will take you farther into space where you will be forever lost.")
    print("Lastly, the fourth one will take you back in time, before the war with space cowboys started.")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2" and path != "3" and path != "4": # input validation
        path = input("Which path will you choose? (1 or 2 or 3 or 4): ")

    return path

def checkPath(chosenPath):
    print("You are in your space craft flying through space...")
    time.sleep(2)
    print("You pass by a lifeless planet nearby that looks rather familiar ...")
    time.sleep(2)
    print("But your skin begins to tingle...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 4)

    if chosenPath == str(correctPath):  #use str to ensure that the chosen path is being compared as a string
        print("That tingling was just the feeling of admiration from the citizens of the galaxy!")
        print("You made it safely back on your home planet, HTRAE")
        print("WELCOME HOME")
    elif chosenPath == str(correctPath):
        print("An energetic burst of gamma rays pass through you.")
        print("Causing all of the atoms in your body to dissolve.")
        print("There is no record left of your existence")
    elif chosenPath == str(correctPath):
        print("Alarms start blaring in your spacecraft, you struggle to see what is going on.")
        print("All of a sudden the button that can launch you lightyears away is activated.")
        print("You try to stop it but it doesn't work...")
        print("Your spacecraft launches you lightyears away knocking you unconscious.")
        print("When you wake up, everything is black. Nothing works...")
        print("you are forever lost...")
    else:
        print("You feel a tingling sensation, looking down you see yourself starting to break away in pieces.")
        print("Beginning to freak, you look around frantically and see that other objects are disappearing too.")
        print("Then everything fades to black...later you wake up and you are back on the mother space station.")
        print("You see a few people run by your room and get up frantically looking for the time and date of today")
        print("It's now Janurary 20, 3035. 10 years before the war started")
        print("What you choose to do is up to you...")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) 
    playAgain = input ("Do you want ot play again? (yes or y to continue playing): ")