# Lesson 30
patternNum = 6
for i in range (1,patternNum+1):
    thingymablobber = ""
    for j in range (1, i+1):
        if j%2==1:
            thingymablobber += "1"
        else:
            thingymablobber +="0"
    print (thingymablobber)