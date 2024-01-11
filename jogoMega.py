import random

def CreateLottery(numbers):
    lottery = []
    while len(lottery) < numbers:
        chosenNumber = random.randint(1,60)
        if chosenNumber in lottery:
            pass
        else:
            lottery.append(chosenNumber)
    lottery.sort()
    return lottery
    
print(CreateLottery(6))