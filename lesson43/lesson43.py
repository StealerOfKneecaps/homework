# Lesson 43
#remove dupes, every unique letter, amount of times the set is the same

def dupli_remover(set):
    newSet = []
    for element in set:
        if element not in newSet:
            newSet.append(element)
    return newSet

def all_unique_letters(word):
    newWord = ""
    for chara in word:
        if chara not in newWord:
            newWord+=chara
    return newWord

def all_intersects(setA, setB):
    count = 0
    allInters = ""
    for ele in setA:
        if str(ele) not in allInters and ele in setB:
            allInters+=str(ele)
            count+=1
    return count

print (dupli_remover([1, 1, 1, 2, 3, 3, 4, 5, 5]))
print (all_unique_letters("abeabenabemabel"))
print (all_intersects([1, 2, 3, 4, 5],[3, 1, 6, 7, 8]))
