# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from point import Point
from shapes import Circle
# Create a Point object for the centre of the circle
circle = Circle(Point(3, 4), "red", 5)

print(f"Position: {circle.position}")
print(f"Colour: {circle.colour}")
print(f"Radius: {circle.radius}")
# Test the area and perimeter methods
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")
# Test inherited methods from Shape class
circle.set_position(Point(0, 0))
print(f"New Position: {circle.position}")

circle.set_colour("blue")
print(f"New Colour: {circle.colour}")
# Test changing the radius
circle.set_radius(2)
print(f"New Radius: {circle.radius}")
print(f"New Area: {circle.area()}")
