import random

# Line 1: random.randint(5, 20)
# What did you see on line 1? → Example output: 13, 7, 20 (run multiple times)
# Smallest seen: 5
# Largest seen: 20
print(random.randint(5, 20))


# Line 2: random.randrange(3, 10, 2)
# What did you see on line 2? → Example output: 3, 5, 9 (run multiple times)
# Smallest seen: 3
# Largest seen: 9
# Could this produce a 4? → No, because it only picks odd numbers: 3, 5, 7, 9
print(random.randrange(3, 10, 2))


# Line 3: random.uniform(2.5, 5.5)
# What did you see on line 3? → Example output: 3.42, 4.98, 2.76 (run multiple times)
# Smallest seen: 2.5
# Largest seen: 5.5
print(random.uniform(2.5, 5.5))

# Random number between 1 and 100 inclusive:
print(random.randint(1, 100))
