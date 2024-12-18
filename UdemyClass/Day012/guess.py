import random

logo = r'''
  ________                                __  .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/       
'''



print(logo)

print("Welcome to the Number Guessing Game!")


secret_number = random.randint(1,100)

guess_attempts = 0
user_guess = 0

print("I'm thinking of a number between 1 and 100.")

difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_choice == "easy":
    guess_attempts = 10
else:
    guess_attempts = 5
    
while guess_attempts > 0 and secret_number != user_guess:
    print(f"You have {guess_attempts} remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    
    if user_guess > secret_number:
        print("Too high.")
        print("Guess again.")
        guess_attempts -= 1
    elif user_guess < secret_number:
        print("Too low.")
        print("Guess again.")
        guess_attempts -= 1
        

if secret_number == user_guess:
    print("You guessed correctly!")
else:
    print(f"You guessed incorrectly - {secret_number}")
    


