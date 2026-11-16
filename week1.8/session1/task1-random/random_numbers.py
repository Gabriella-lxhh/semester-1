import random

# Get user to input how many random numbers they want
number = int(input("How many random numbers do you want? "))
# Generate this many random numbers
numbers = []
for i in range(number):
    numbers.append(random.randint(1, 200))
# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")
