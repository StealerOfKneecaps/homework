# Lesson 8
#remember doing this is Java lol    
wCounter = 0
for _ in range (0,6):
    wOrL = input("Hey yo (all lower case) bruh w or l ")
    if wOrL=="w" or wOrL=="W":
        print("broo that's crazy bro")
        wCounter+=1
if wCounter == 6 or wCounter == 5:
    print("group 1")
elif wCounter == 4 or wCounter == 3:
    print("group 2")
elif wCounter == 2 or wCounter ==1:
    print("group 3")