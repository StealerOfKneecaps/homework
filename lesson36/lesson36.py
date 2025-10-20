# Lesson 36
def is_prime(argPrime):
    for i in range (2, int(argPrime**0.5//1+1)):
        if argPrime%i==0:
            return False
    return True

for j in range (1, 10001):
    if is_prime(j):
        print(j)

argFact = 25
for i in range (1, int(argFact**0.5//1+1)):
    if argFact%i==0 and int(argFact/i) != int(i):
        print(i)
        print(argFact/i)         
    elif argFact%i==0:
        print(i)