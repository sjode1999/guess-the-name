# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import sys


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x/y


print("User Menu")
print("1. to add ")
print("2. to subtract")
print("3. to multiply")
print("4. to divide")
print("5. to exit")

while True:
    choice = int(input("Enter Choice (1/2/3/4/5): "))

    if choice == 5:
        print("Thank you for using calculator!!!")
        break

    if choice not in (1, 2, 3, 4):
        print("Invalid Selection, Please Try Again")
        continue

    num1 = int(input("Enter the first number: "))
    while True:
        num2 = int(input("Enter the second number: "))
        if choice == 4 and num2 == 0:
            print('Cannot divide by 0. Are you dumb?')
            continue
        else:
            break

    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == 4:
        print(num1, "/", num2, "=", divide(num1, num2))

    while True:
        another_calculation = input("Would you like to make a new calculation (Y/N): ")
        if another_calculation.upper() == "N":
            sys.exit()
        if another_calculation.upper() == "Y":
            break
        print("Invalid Selection")
        continue

        print('hello')