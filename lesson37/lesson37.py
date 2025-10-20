# Lesson 37
def string_zipper(zipped):
    returner = zipped[0]
    prevChar = zipped[0]
    counter=0
    totalCount = 0
    for char in zipped:
        if char==prevChar:
            counter+=1
            totalCount+=1
        else:
            totalCount+=1
            prevChar = zipped[totalCount]
            returner += str(counter)
            counter = 1
            returner += char
    returner+=str(counter)
    return returner
print(string_zipper("aaabbbbcccccdd"))