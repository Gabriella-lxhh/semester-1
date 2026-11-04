# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    def __init__(self, name, birth):
        """Initialize the person's name and date of birth."""
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(birth, date):
            raise TypeError("birth must be a date object")
        if name == "":
            raise ValueError("name must not be empty")
        self.name = name
        self.birth = birth

    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """
        Return the initials of the person."""
        result = ""
        for part in self.name.split():
            result += part[0].upper()
        return result
    def is_birthday(self):
        """
        Return whether today is the person's birthday."""
        today = date.today()
        return(
            self.birth.month == today.month and self.birth.day == today.day
        )
