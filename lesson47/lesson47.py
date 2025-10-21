# Lesson 
#we got an easy one after that goddayum one last time
def factorail_but_addition(numberToBeFactorialed):
    sum = 0
    for i in range (numberToBeFactorialed, 0, -1):
        sum += i
    return sum
print (factorail_but_addition(1000000))#this is pretty fast actually