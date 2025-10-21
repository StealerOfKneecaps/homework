# Lesson 23
sum = 0
count = 0
while True:
    
    res = input("hey brosephine gimme a number (if it's \"stop\" I'll stop)")
    if res=="stop":
        break
    else:
        sum+=int(res)
        count+=1
print (sum/count)