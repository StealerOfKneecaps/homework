# Lesson 38
def is_palin(palArg):
    if str(palArg)[:]== str(palArg)[::-1]:
        return True
    return False
listOfPalins = []
for i in range (100, 1000):
    for j in range (100, 1000):
        if is_palin(i*j):
            listOfPalins.append(i*j)
print (max(listOfPalins))