# Lesson 20
def perf_numbrero(num):
    sum = 0
    for i in range (1, int(num//2)+1):
        if num%i==0:
            sum+=i
    return sum==num
for i in range (0,10000):
    if perf_numbrero(i):
        print(i)