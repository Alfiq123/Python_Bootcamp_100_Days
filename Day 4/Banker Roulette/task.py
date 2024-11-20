import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

who = random.randint(0, 4)

print(friends[who])
print(random.choice(friends))
