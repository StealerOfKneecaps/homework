# Lesson 27
def cleaner_upper(needsCleaning):
    new = ""
    for chara in needsCleaning:
        if chara.isalpha():
            new+=chara
    return new
print (cleaner_upper("A2471894yh9efr8*"))