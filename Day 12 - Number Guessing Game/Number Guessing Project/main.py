import art
import random

print(art.logo)
print("Welcome to The Number Guessing Game!")
difficulty = input("\nWhat difficulty would you like to choose? 'easy' or 'hard': ").lower()

print("\nI'm guessing a number between 0 and 100..")

num = random.randint(0,100)

Game = True

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Wrong input. Try again")

while Game and attempts > 0:
    try:
        user_guess = int(input(f"\nYou have {attempts} attempts left\nWhat's your guess?: "))
    except ValueError:
        print("Wrong input. Please try again.")
        continue

    if user_guess == num:
        print(f"You got it right! The number was {num}")
        Game = False
    elif user_guess > num:
        print("Too high. Try again")
    else:
        print("Too low. Try again")

    attempts -= 1

    if attempts == 0 and user_guess is not num:
        print(f"You are out of guesses. The number was {num}")
        Game = False






