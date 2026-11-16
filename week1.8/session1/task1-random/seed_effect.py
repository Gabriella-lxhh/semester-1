# See README.md for instructions on what to do this program

import random

random.seed(27)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)
# Using the same seed produces the same sequence of random numbers.
# Changing the seed changes the sequence.
# Without a fixed seed, the results usually differ between runs.