print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: $"))
tip = int(input("What percentage tip would you like to give?: 10 12 15 "))
people = int(input("How many people to split the bill?: "))

bill_tip = bill * (tip / 100) + bill
people_pay = bill_tip / people

print(f"Each Person Should Pay ${round(people_pay, 2)}")
