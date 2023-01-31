#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
        size (int): The size of the new square.
        """
        self.__size = size

    # Property
    @property
    def size(self):
    """int: private size.

    Returns:
        Private size.
    """
        return self.__size

    # Setter modifies
    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value (int): size of the square.
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """returns the area

        Returns:
            area.
        """
        return self.__size**2
