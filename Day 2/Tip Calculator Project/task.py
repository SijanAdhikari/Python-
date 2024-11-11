print("Welcome to the tip calculator!")
bill=float(input("What was the total bill?\n"))
tip=float(input("How much tip would you like to give? 10,12 or 15\n"))/100
total_bill=bill+bill*tip
no_of_people=int(input("How many people to split the bill?\n"))
bill_for_each_person=round(total_bill/no_of_people)
print(f"Each person should pay:{bill_for_each_person}")