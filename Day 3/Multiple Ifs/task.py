print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("YOU CAN RIDE THE ROLLERCOASTER")
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill=5
        print(f"CHILD TICKETS ARE ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"YOUTH TICKETS ARE ${bill}.")
    else:
        bill = 12
        print(f"ADULT TICKETS ARE ${bill}.")
    photo=int(input("Do you want to capture your rollercoaster moment?        PRESS______ 1 ___if yes and PRESS____0____if no\n"))
    if photo==1:
        bill+=3
        print(f"Total bill is ${bill}")
    else:
        print("Invalid input. RETRY")

else:
    print("Sorry you have to grow taller before you can ride.")
