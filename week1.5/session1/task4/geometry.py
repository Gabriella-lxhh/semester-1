# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """A point in 2D space."""

    def __init__(self, x, y):
        """
        Create a point with x and y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self):
        """Return the distance from this point to the origin."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance_to(self, other):
        """
        Return the distance from this point to another point.
        """
        return math.sqrt(
            (other.x - self.x) ** 2 + (other.y - self.y) ** 2
        )
# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle
class Circle:
    """
    A circle with a centre and radius.
    """

    def __init__(self, centre, radius):
        """
        Create a circle with the given centre and radius.
        """
        self.centre = centre
        self.radius = radius

    def area(self):
        """
        Return the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Return the perimeter of the circle.
        """
        return 2 * math.pi * self.radius
# Don't add any testing code to this file!
