# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not isinstance(width, int):
            raise TypeError("width must be an int")
        if not isinstance (height, int):
            raise TypeError("height must be an int")
        if width <= 0:
            raise ValueError("width must be greater than 0")
        if height <= 0:
            raise ValueError("height must be greater than 0")

        self.width = width
        self.height = height
        # raising appropriate exceptions if necessary (see README.md)
       
    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        """
        Return whether the rectangle is a square."""
        return self.width == self.height
    def area(self):
        """
        Return the area of the rectangle."""
        return self.width * self.height
    def perimeter(self):
        """
        Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
