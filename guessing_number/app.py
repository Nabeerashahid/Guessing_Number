#PROJECT 2
# 1 to 100 numbers

import random
def guess_the_number():
    number = random.randint(1, 100)
    guesses_left = 7
    #Welcome message
    print("Welcome to the guessing number game")
    
    while guesses_left > 0:
        print(f"\n Yu have {guesses_left} guesses left. ")
        try:
            guess = int(input("Take a guess of another number : "))
        except ValueError: 
            print("Invalid input: please enter a  number : ")
            continue
        
        #guess the secret number 
        if guess < number:
            print("Too Low Number! Tell another ")
        elif guess > number:
            print("Too high Number! Tell another")
        else:
            print(f"Congratulations! you got the correct number in {7 - guesses_left + 1 } tries ")
            return
        guesses_left -= 1
    print(f"\n you ran out of guess. the number was {number}.")
        
guess_the_number()    