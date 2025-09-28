# Lesson 13
monthNumber =  int(input("What's the month? number"))
if monthNumber>2:
    print("After feb18")
elif monthNumber<2:
    print("Before feb18")
else:
    dayNumber = int(input("What's the day?"))
    if dayNumber>18:
        print("After 18th")
    elif dayNumber<18:
        print("Before 18th")
    else:
        print("On 18th")