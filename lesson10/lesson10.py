# Lesson 10
teleNumber = input("What is the number that you want to know if telemarketer or no? last 4 digits\n")
if (teleNumber[0]=="8" or teleNumber[0]=="9") and (teleNumber[1]==teleNumber[2]) and (teleNumber[3]=="8" or teleNumber[3]=="9"):
    print("yea it's a marketer lmao block their ah")
else:
    print("nah it's not a marketer")