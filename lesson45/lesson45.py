# Lesson 45
def word_list_counter(wordList):
    wordAndCount = {}
    for stri in wordList:
        wordAndCount [stri] = len(stri)
    return wordAndCount

def fib_dict_maker(nTerm):
    fibDict = {}
    for i in range (0, nTerm):
        fibDict [i] = fib_returner(i)
    return fibDict

def fib_returner(otherNTerm):
    if otherNTerm == 0:
        return 0
    elif otherNTerm == 1:
        return 1
    else:
        return fib_returner(otherNTerm-1) + fib_returner(otherNTerm-2)

print (word_list_counter(["Rimeu","Marisa","Skukuy"]))
print (fib_dict_maker(10))