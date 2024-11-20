import random
import alaska

ran_int = random.randint(1, 10)
print(ran_int)

print()

print(alaska.var_a)
print(alaska.var_b)
print(alaska.var_c)

print()

ran_ran = random.random() * 12
print(ran_ran)

print()

ran_uni = random.uniform(1, 10)
print(ran_uni)

print()

# Pause 1 - Heads or Tails

# head = "Heads"
# tail = "Tails"
choose = random.randint(0, 5)

if choose in (0, 1, 2):
    print("Heads")
else:
    print("Tails")
