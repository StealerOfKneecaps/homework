# Lesson 46
#I really don't wanna
def next(prev):
    if prev%2==0:
        return int(prev/2)
    else:
        return int(prev*3+1)
iDefinitelyDidntChatGPTThis = {1:1}

def chain_length_finder(argNum):
    if argNum in iDefinitelyDidntChatGPTThis:
        return iDefinitelyDidntChatGPTThis[argNum]
    else:
        counter = 0
        originalSoICouldIndexItAndItWontBeAtOne = argNum
        while (argNum!=1):
            argNum=next(argNum)
            counter+=1
        iDefinitelyDidntChatGPTThis[originalSoICouldIndexItAndItWontBeAtOne] = counter 
    return counter

#oh sweet pale king have mercy

largest = 0
largestKey = 0

for number in range (1, 1001):
    if chain_length_finder(number)>largest:
        largest = chain_length_finder(number)
        largestKey = number
print (f"largest chain is {largestKey} with a length of {largest}")

#Apparently you can do this faster but I honestly don't really care D: I don't wanna figure it ouuuuuuuuut