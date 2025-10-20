# Lesson 44
def dict_maker(aString):
    sortedString = sorted(aString.lower())
    answer = {}
    for chara in sortedString:
        if chara not in answer:
            answer[character] = 1
        else:
            answer[character] += 1
    return answer