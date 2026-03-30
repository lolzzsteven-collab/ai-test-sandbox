import random

def start_game():
    print("Welcome to Guess The Number Game!")
    
    number = random.randint(1, 50)
    attempts = 0
    
    while attempts < 5:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess == number:
            print("You guessed it right!")
            break
        
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")
        
        attempts = attempts + 1
        
        if attempts == 5:
            print("Game Over! The number was " + str(number))

start_game()