# Lesson 40
def is_prime(lordofthemysteriesiskindabad):
    for i in range (2, int(lordofthemysteriesiskindabad**0.5//1+1)):
        if lordofthemysteriesiskindabad%i==0:
            return False
    return True
for i in range (1, 10001):
    if is_prime(i):
        print(i)