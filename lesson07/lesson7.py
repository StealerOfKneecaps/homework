# Lesson 
#This'll be a pain
import random
diffCheck = int(input("Yo what's the dc yo"))
diceRoll = random.randrange(1,21)
print (f"The roll was {diceRoll}" )
if diffCheck>= diceRoll:
    print ("you FAILED LMAOOOOO")
else:
    print ("eh you won")