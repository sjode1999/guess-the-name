import random

def Guess_Game():
    print("Welcome to the guessing game")
    Real_Number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            Guess_Number = int(input("Guess the number between (1 and 10): "))
        except ValueError:
            print('Invalid input. Please enter a valid number.')
            continue

        attempts += 1

        if Guess_Number == Real_Number:
            print(f"Congratulations, you guessed in {attempts} attempts.")
            break
        elif Guess_Number < Real_Number:
            print("Wrong Answer! Try Higher.")
        else:
            print("Wrong Answer! Try Lower.")

    while True:
        Another_attempt = input('Would you like to try again (Y/N): ')
        if Another_attempt.upper() == 'N':
            break
        elif Another_attempt.upper() == 'Y':
            break
        else:
            print('Invalid Selection')

if __name__ == "__main__":
    Guess_Game()