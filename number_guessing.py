"""
This file contains an incomplete function definition.  
Your task is to complete the incomplete function definition. so that it behaves as indicated in the documentation.

Do not run this file directly.
Rather, call this function from main.py and run that file.
"""
import random
#is this neccesary? different way to do it?

def guess_number(low, high, num_attempts):
    """
    This function, named 'guess_number', generates a psudo-random integer in a given range, inclusive.
    The user is given a certain number of attempts to guess the correct number.
    The function prints the range to the user and informs the user of how many attempts they have.
    The function asks the user to guess the number the given number of times.
    You must use the random module's randint function to generate the pseudo-random integer.
    You must use a for loop to give the user multiple attempts.
    If the user enters a non-numeric response, the program must not crash, but simply count that as an incorrect answer.
    If the user guesses any attempt correctly, the function immediately exits the loop and returns True.
    If the user enters all attempts incorrectly, the function returns False.

    :param low: The low end of the range in which the pseudo-random number is generated.
    :param high: the high end of the range in which the pseudo-random number is generated.
    :param num_attempts: The number of attempts the user is given to guess the correct number.
    :returns: True if the user answers any attempt correctly, False otherwise.
    """
    
    random_num = random.randint(low, high)
    print(f"The range including the random number is {low} to {high}. You have {num_attempts} attempts to guess it.")
    for i in range(num_attempts):
        guess = input(f"Enter guess number {i + 1}: ")
        if guess.isdigit():
            guess = int(guess)
            if guess == random_num:
                return True
            else:
                continue
    return False


