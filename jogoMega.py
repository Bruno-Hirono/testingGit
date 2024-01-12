import random


'''Brazilian main lottery (mega sena) is composed of 6 numbers chosen between 1 and 60. '''


def CreateLotteryNumbers(quantityNumbers=6, listNumbers=[]):
    """Creates a random lottery numbers list. The two optional variables are the quantity of numbers (min = 6; max = 15) and \
    a list of manually choosen numbers.
    If no argument is passed, a smallest available list of numbers (06) will be returned"""
    
    #%%
    """ First block of code for checking user errors using python´s try-assert-except"""
    # Check for correct fisrt variable formats
    try:
        assert isinstance(quantityNumbers, int) and quantityNumbers>5 and quantityNumbers<61
    except:
        return "First variable must be a integer between 6 and 15 (default is 6)."
        
    # Check if second variable is a list
    try:
        assert type(listNumbers) == type(list())
    except:
        return "Second variable must be a list of integers (default is an empty list)."
    
    # Check each element in listNumbers if it is a numeric values
    try:
        for number in listNumbers:
            assert isinstance(number, int) and number<=60 and number>=1
    except:
        return "The list must contain only integers between 1 and 60"    
    
    # Check if the listNumbers has duplicates
    try:
        withoutDuplicates = set(listNumbers)
        assert len(withoutDuplicates) == len(listNumbers)
    except:
        return "The list must have unique integers"
    
    #%%
    """ Second block of code for checking user errors using if-elif-else"""
    # Check if quantity of numbers is within avaliable lottery posibilities
    if quantityNumbers < 6 or quantityNumbers > 15:
        return "Avaliable lottery numbers are limited to a quantity between 06 and 15."
    
    # Check if listNumbers is smaller than passed quantityNumbers
    if len(listNumbers) > quantityNumbers:
        return "Quantity of numbers must be equal or bigger than passed listNumbers with previosly choosen numbers."
    
    if len(listNumbers)>0:
        # Check if manully choosen numbers are within the lottery avaliable range (1 <= x <= 60)
        if max(listNumbers) > 60:
            return "Lottery numbers must be within 1 to 60 range. Empty list for 100% computer generated numbers."
    
    #%%
    """Third block is where the random numbers are being generated"""
    
    # While there is still avaliable slots for random numbers, choose one from within range.
    while len(listNumbers) < quantityNumbers:
        chosenNumber = random.randint(1,60)
        # Check if most recent random number is already in the listNumbers, if so, pass without using the repeated number.
        if chosenNumber in listNumbers:
            pass
        # If number is not repeated, append to the listNumbers
        else:
            listNumbers.append(chosenNumber)
            
    listNumbers.sort() # Sort is used to sequence the numbers in increasing order.
    
    
    return listNumbers
    

#print(CreateLotteryNumbers(6)) 