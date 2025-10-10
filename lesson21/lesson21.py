# Lesson 21
def greatestIn(theNumber):
    curretnGreat = 0
    biggestNum = 0
    for i in range(1, theNumber+1):
        factNum = 0
        for j in range (1, i+1):
            if i%j==0:
                factNum+=1
        if factNum>=curretnGreat:
            curretnGreat = factNum
            biggestNum = i
    return biggestNum
print (greatestIn(52))