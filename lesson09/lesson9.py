import random
# Lesson 
# yo it's roshambo
dictOfWhoBeatsWho = {
    "r":"s",
    "p":"r",
    "s":"p"
}
wannaContinue = "y"
while (wannaContinue == "y"):
    aiChoice = random.choice(["r", "p", "s"])
    playerChoice = input("yo bro roshambo time what do you chcoose r p or s").lower()
    if playerChoice == aiChoice:
        print ("draw.")
    elif dictOfWhoBeatsWho[aiChoice] == playerChoice:
        print ("fricken loser lmao")
    else:
        print ("WOW you WON you GENIUS")
    wannaContinue = input("Bro wanna go again y/n")