# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Enter your grade (0-100): ")
if not grade.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")
    
grade =int(grade)
if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")
if 0 <=grade <= 39:
    print(f"{grade} is a Fail")
elif 40 <= grade <=69:
    print(f"{grade} is a Pass")
else:
    print(f"{grade} is a Distinction")

