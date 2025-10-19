# Lesson 32

listOne = [0,1,2,3,4]
listTwo = [3,4,5,6,7]
sharedStuff = []
for num in listOne:
    for nummy in listTwo:
        if num==nummy and num not in sharedStuff:
            sharedStuff.append(num)

print (sharedStuff)