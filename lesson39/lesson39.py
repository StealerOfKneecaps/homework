# Lesson 39
def common_finder(first, sec):
    for possFact in range (min(first,sec), 0, -1):
        if max(first,sec)%possFact==0 and min(first,sec)%possFact==0:
            return possFact
    return "None"
print (common_finder(100, 98))