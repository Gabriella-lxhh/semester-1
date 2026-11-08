# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor her
    def __init__(self, x, y):
        """
        Create a point with x and y coordinates.
        """
        self.x = x
        self.y = y
    # Add distance() method here

    def distance(self):
        """
        Return the distance from this point to the origin.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)
    # Add distance_to() method here
    def distance_to(self, other):
        """
        Return the distance from this point to another point.
        """
        return math.sqrt(
            (other.x - self.x) ** 2 + (other.y - self.y) ** 2)
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
#Demonstrate use of Point
p1 = Point(3, 4)
print(f"x: {p1.x}, y: {p1.y}")
print(f"Distance from origin: {p1.distance()}")
p2 = Point(6, 8)
print(f"Distance from p1 to p2: {p1.distance_to(p2)}")
