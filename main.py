# This is a sample Python script.
g
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 10): "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break