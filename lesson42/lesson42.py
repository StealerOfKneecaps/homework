# Lesson 42
def is_sum_of(list,target):
    for i, value in enumerate(list):
        newerTarg = target-value
        if newerTarg in list[i+1:]:
            return True
    return False