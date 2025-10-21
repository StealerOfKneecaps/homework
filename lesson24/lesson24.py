# Lesson 24
longLength = 0
longName = ""
while True:
    inpName = input("hey joseph broseph gimme name '''X''' for stop ")
    if inpName == "X":
        break
    elif len(inpName)>longLength:
        longLength=len(inpName)
        longName = inpName
print(longName)