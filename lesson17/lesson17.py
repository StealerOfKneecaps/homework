# Lesson 17
def fact(num):
    sum = 1
    for i in range (2, num+1):
        sum *= i
    return sum
factRequest = int(input ("bro what number youw ant factyorialdfsds"))
print (fact(factRequest))