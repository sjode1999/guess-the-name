import random
import sys


def guess_the_number():
    print("Welcome to the guess the number game")
    real_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess_number = int(input("Guess the number between (1 and 10): "))
        except ValueError:
            print('Invalid input. Please enter a valid number.')
            continue

        attempts += 1

        if guess_number < real_number:
            print("Wrong Answer! Try Higher.")
            continue
        if guess_number > real_number:
            print("Wrong Answer! Try Lower.")
            continue

        print(f"Congratulations, you guessed the number in {attempts} attempts.")
        while True:
            another_attempt = input('Would you like to try again (Y/N): ')
            if another_attempt.upper() == 'N':
                print('Later gator!')
                sys.exit()
            if another_attempt.upper() == 'Y':
                break

            print('Invalid Selection dumb ass!')
            continue

if __name__ == "__main__":
    guess_the_number()
