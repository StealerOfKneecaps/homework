import random
def splitter(magicThing):
    return magicThing.split(",",-1)
def randomRanger(magicThing2,magicThing3):
    return random.randrange(magicThing2, magicThing3+1)
print (splitter("reimu,is,the,best"))
print (randomRanger(1,5))