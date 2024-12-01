# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# Functions with more than 1 input
# def greet_with(name, location):
#     print(f"Hello Mr.{name}")
#     print(f"You're lived in {location}")
#
# greet_with("Fiber", "Sydney")

# def greet_with(name, location):
#     print(f"Hello Mr.{name}")
#     print(f"You're lived in {location}")
#
# greet_with(location = "Jakarta", name = "Matron")

def calculate_love_score(name_a, name_b):

    zero_a = 0
    zero_b = 0

    for a in name_a + name_b:

        if a in ("T", "t"):
            print("🍎 Got T")
            zero_a += 1

        elif a in ("R", "r"):
            print("🍎 Got R")
            zero_a += 1
            zero_b += 1

        elif a in ("U", "u"):
            print("🍎 Got U")
            zero_a += 1
            zero_b += 1

        elif a in ("E", "e"):
            print("🍎 Got E")
            zero_a += 1
            zero_b += 1

        elif a in ("L", "l"):
            print("🍎 Got L")
            zero_a += 1
            zero_b += 1

        elif a in ("O", "o"):
            print("🍎 Got O")
            zero_a += 1
            zero_b += 1

        elif a in ("V", "v"):
            print("🍎 Got V")
            zero_a += 1
            zero_b += 1

        elif a in ("E", "e"):
            print("🍎 Got E")
            zero_a += 1
            zero_b += 1

        else:
            print(a)

    print()

    print(f"Name A have {zero_a}")
    print(f"Name B have {zero_b}")

    print(str(zero_a) + str(zero_b))

# calculate_love_score("Sabatron", "Enlish")

calculate_love_score("Kanye West", "Kim Kardashian")