from bisect import insort
from random import choice

sides = ["Allied", "Soviets", "Epsilon", "Foehn", "Ambassador", "United"]

print(sides[0])
print(sides[2])
print(sides[4])

sides.append("Integrum")
sides.extend(["Sodium", "Non-Americans", "Civilian"])
sides.insert(0, "Arands")

# sides.pop(1)
# sides.clear()

# sides.count("Allied")

# chosen = str(input("Enter the choice, y or n: ")).lower()

# while chosen == "y":
#     sides.pop(0)
#     print(sides)
#     chosen = str(input("Enter the choice, y or n: "))
#     continue

print(sides)