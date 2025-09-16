# Lesson 3
#Yall idk if we're allowed to use math import??? it WOULD however make this SO EASY so I'm using it
import math
def Main():
    amountOfSquares = int(input("Yo how many squares you got yo")) 
    sideLength = (math.sqrt(amountOfSquares))//1
    print(f"The largest possible square has an area of {sideLength**2} and has a sidelength {sideLength}")
Main()