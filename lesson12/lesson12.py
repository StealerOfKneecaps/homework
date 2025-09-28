# Lesson 
#The legendary triangle question
print("Hi! I will determine if your triangle is equil., scal., or iso.")
angleA = int(input("What is your first angle\n"))
angleB = int(input("What is your second angle\n"))
angleC = int(input("What is yoru third angle\n"))
if angleA+angleB+angleC!= 180:
    print("Nice try sucker ")
elif angleA==angleB==angleC:
    print("Equilateral!")
elif angleA!=angleB!=angleC:
    print("Isosceles!")
else:
    print("Scalene!")