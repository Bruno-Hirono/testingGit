import random


'''Brazilian main lottery (mega sena) is composed of 6 numbers chosen between 1 and 60. '''


def CreateLotteryNumbers(quantityNumbers=6, list=[]):
    """Creates a random lottery numbers list. The two optional variables are the quantity of numbers (min = 6; max = 15) and \
    a list of manually choosen numbers.
    If no argument is passed, a smallest available list of numbers (06) will be returned"""
    
    
    # Check if quantity of numbers is within avaliable lottery posibilities
    if quantityNumbers < 6 or quantityNumbers > 15:
        return "Avaliable lottery numbers are limited to a quantity between 06 and 15."
    
    # Check if list is smaller than passed quantityNumbers
    if len(list) > quantityNumbers:
        return "Quantity of numbers must be equal or bigger than passed list with previosly choosen numbers."
    
    # Check if manully choosen numbers are within the lottery avaliable range (1 <= x <= 60)
    if min(list) < 1 or max(list) > 60:
        return "Lottery numbers must be within 1 to 60 range."
    
    # While there is still avaliable slots for random numbers, choose one from within range.
    while len(list) < quantityNumbers:
        chosenNumber = random.randint(1,60)
        # Check if most recent random number is already in the list, if so, pass without using the repeated number.
        if chosenNumber in list:
            pass
        # If number is not repeated, append to the list
        else:
            list.append(chosenNumber)
            
    list.sort() # Sort is used to sequence the numbers in increasing order.
    
    
    return list
    

#print(CreateLotteryNumbers(6)) 