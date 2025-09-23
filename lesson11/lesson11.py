# Lesson 11
xCoordYCoord = input("What are the coordinates")
(x, y) = xCoordYCoord.split(",") #Whenever there's a comma, it splits it
#you are splitting it into variables x and y

if int(x)>0 and int(y)>0:
    print ("q1")
elif int(x)>0 and int(y)<0:
    print("q4")
elif int(x)<0 and int(y)>0:
    print ("q2")
elif int(x)<0 and int(y)<0:
    print ("q3")
else:
    print ("it's on one of the axes")
