import random


'''Brazilian main lottery (mega sena) is composed of 6 numbers chosen between 1 and 60. '''
def CreateLotteryNumbers(numbers=6, list=[]):
    "Creates a random lottery numbers list. Variables are the quantity of numbers (min = 6; max = 15) and a list of \
    chosen numbers (non-random)"
    if numbers < 6 or numbers > 15:
        return "Avaliable lottery numbers are limited to a quantity between 06 and 15."
    lottery = list
    while len(lottery) < numbers:
        chosenNumber = random.randint(1,60)
        if chosenNumber in lottery:
            pass
        else:
            lottery.append(chosenNumber)
    lottery.sort()
    return lottery
    

#print(CreateLotteryNumbers(6))