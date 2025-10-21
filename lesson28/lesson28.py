# Lesson 28
def palin_checker(probPalin):
    if probPalin[:]==probPalin[::-1]:
        return True
    return False
print (palin_checker("efFfe"))