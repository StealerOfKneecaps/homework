# Lesson 
def is_prime(primeCheck):
    for i in range (2,int(primeCheck**0.5//1+1)):
        if primeCheck%i==0:
            return False
    return True

def large_finder(largeFindee):
    largest = 0
    for i in range (1, largeFindee+1):
        if is_prime(i) and i>largest and largeFindee%i==0:
            largest = i
    return largest
print (large_finder(27))