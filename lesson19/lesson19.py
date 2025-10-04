import math
def isPrime(primeCheck):
    if primeCheck ==1:
        return False
    for i in range (2, math.floor(primeCheck**0.5)+1):
        if primeCheck%i==0:
            return False
    return True
primeChecker = int(input("heyo what number you need check ed"))
if isPrime(primeChecker):
    print("yea bro that's a prime")
else:
    print("nah bro that's not a prime")