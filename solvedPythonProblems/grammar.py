import random

rules = [ "[INTEGER]", "[NESTED_LIST, INTEGER]", "[INTEGER, NESTED_LIST]", "NESTED_LIST + NESTED_LIST"]

def generateRandomNumber():
    return random.randrange(1, 20)

def generateRandomNestedList():
    random_rule = random.randrange(4)
    if random_rule == 0:
        return [generateRandomNumber()]

    elif random_rule == 1:
        return [generateRandomNestedList(), generateRandomNumber()]

    elif random_rule == 2:
        return [generateRandomNumber(), generateRandomNestedList()]

    elif random_rule == 3:
        return generateRandomNestedList() + generateRandomNestedList()

print(generateRandomNestedList())