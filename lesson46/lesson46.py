# Lesson 46
#I really don't wanna
def next(prev):
    if prev%2==0:
        return int(prev/2)
    else:
        return int(prev*3+1)
iDefinitelyDidntChatGPTThis = {1:1}

def chain_length_finder(argNum):
    original = argNum
    steps = 0
    while argNum not in iDefinitelyDidntChatGPTThis:
        argNum = next(argNum)
        steps +=1
    length = steps + iDefinitelyDidntChatGPTThis[argNum]
    iDefinitelyDidntChatGPTThis[original] = length
    return length
    # if argNum in iDefinitelyDidntChatGPTThis:
    #     return iDefinitelyDidntChatGPTThis[argNum]
    # else:
    #     counter = 0
    #     eee = argNum
    #     while (argNum!=1):
    #         argNum=next(argNum)
    #         counter+=1
    #     iDefinitelyDidntChatGPTThis[eee] = counter 
    # return counter
#above shit didn't work so I had to chatgpt it again
largest = 0
largestKey = 0

for number in range (1, 1000001):
    if chain_length_finder(number)>largest:
        largest = chain_length_finder(number)
        largestKey = number
print (f"largest chain is {largestKey} with a length of {largest}")

