# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
numbers = read_numbers()
if len(numbers) == 0:
    print("Error: no numbers provided", file=sys.stderr)
    sys.exit(1)

minimum = min(numbers)
maximum = max(numbers)
print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
mean = sum(numbers) / len(numbers)
print(f"Mean = {mean}")
numbers.sort()
n = len(numbers)
if n % 2 == 1:
    median = numbers [n // 2]
else:
    median = (numbers [n // 2 - 1] + numbers [n // 2]) /2
print(f"Median = {median}")

