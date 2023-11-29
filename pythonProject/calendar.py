#"I Used datetime import not calendar because datetime specifies the year,day,month while calendar is used to create an actual calendar"


from datetime import datetime



def time():
    return("%H:%M:%S")

def day():
    return("%D")

def month():
    return("%B")

def year():
    return("Year")

now = datetime.now()

print("Menu")
print("1. Time")
print("2. Day")
print("3. Month")
print("4. Year")
print("5. Exit Calendar")

while True:
    try:

        choice = int(input("Choose (1/2/3/4): "))
    except ValueError:
        print("Not a valid selection")

    if choice == 5:
        print("Thank you for using calendar")
        break

    if choice not in (1, 2, 3, 4):
        print("Enter a valid selection")
        continue

    if choice == 1:
        print("Today's Time:", now.strftime("%H:%M:%S"))

    elif choice == 2:
        print("Today's Day", now.strftime("%D"))

    elif choice == 3:
        print("Current Month:", now.strftime("%B"))

    elif choice == 4:
        print("Current Year:", now.year)


    if __name__ == "__main__":
        time(),day(), month(), year()
