print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? Small, Medium or Large: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Yes or No: ").lower()
extra_cheese = input("Do you want extra cheese? Yes or No: ").lower()

bill = 0

if size in ("s", "small"):
    bill = 15

    if pepperoni in ("y", "yes"):
        bill += 2

elif size in ("m", "medium"):
    bill = 20

    if pepperoni in ("y", "yes"):
        bill += 3

if size in ("l", "large"):
    bill = 25

    if pepperoni in ("y", "yes"):
        bill += 3

if extra_cheese in ("y", "yes"):
    bill += 1

print(f"Your final bill is: ${round(bill, 2)}.")



print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
