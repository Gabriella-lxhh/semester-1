# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum
from money import Money
# Create two Money objects
money1 = Money(3, 75)
money2 = Money(2, 50)

print(money1)
print(money2)
# Add them together and print the sum
total = money1 + money2
print(total)