# Lesson 35
def dupeRemover(magicThing):
    newList = []
    for thing in magicThing:
        if thing not in newList:
            newList.append(thing)
    return newList
print (dupeRemover(["reimu", "reimu", "reimu", "sakuya","marisa","reimu","sanae"])) 