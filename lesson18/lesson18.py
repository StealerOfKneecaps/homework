import math
factoredNum = int(input("Hey bro what number youw ant the factors of"))
for i in range (1, math.floor(factoredNum**0.5)+1):
    if factoredNum%i == 0 and i**2!=factoredNum:
        print (i)
        print (factoredNum/i) 
    elif factoredNum%i==0:
        print (i)
        