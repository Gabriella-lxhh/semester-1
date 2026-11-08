# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import Point, Circle
# Create a Circle object
centre = Point(0, 0)
circle = Circle(5, centre)
# Create some Point objects to test
print(Point(3, 4) in circle)  # Should be True (inside the circle)
print(Point(5, 0) in circle)  # Should be True (on the edge of the circle)
print(Point(6, 0) in circle)  # Should be False (outside the circle)