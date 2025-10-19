# Lesson 33
thing = [1, 2, 3, 4, 5, 6, 7, 8]
def meanFinder(thing1):
    sum = 0
    numofnums = len(thing1)
    for num in thing1:
        sum+=num
    return sum/numofnums
def medianFinder(thing2):
    listy2 = sorted(thing2)
    if len(listy2)%2==0:
        firstAvg = listy2[int(len(listy2)/2)-1]
        secAvg = listy2[int(len(listy2)/2+1)-1]
        return (firstAvg+secAvg)/2
    else:
        return int(listy2[int(len(listy2)//2+1)])
print(meanFinder(thing))
print(medianFinder(thing))