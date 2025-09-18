import math
# Lesson 4 yall apparently .length is len in python idk how I feel about taht bro
lengthOne = input("How long is the first section of fence?\n")
lengthTwo = input("How long is the second section of fence?\n")
lengthThr = input("How long is the third section of fence?\n")
totalLength = len(lengthOne)+len(lengthTwo)+len(lengthThr)
timesToBuyPain = math.ceil(totalLength/12)
cost = (round((timesToBuyPain*14.95)*100))/100
#guys this is just rounding it to 2 decimal places don't worry guys
bucketsLeft = timesToBuyPain*12-totalLength
print(f"you need {totalLength} buckets.\n you would have {bucketsLeft} buckets left.\n it would cost ${cost}.")