# Lesson 
#ok I'm gonna redo these beacuse it's like 7 quesions total

def fibo_finder(fiboArger):
    if fiboArger ==0:
        return 0
    elif fiboArger==1:
        return 1
    else:
        return fibo_finder(fiboArger-1) + fibo_finder(fiboArger-2)
print (fibo_finder(25))