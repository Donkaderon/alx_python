"""
The square module provides a class to represent a square shape.

Module: square

Classes:
    Square: Represents a square shape.

"""

class Square:
    """
    Square class represents a square shape.

    Attributes:
        __size (int): Private instance attribute representing the size of the square.

    Methods:
        __init__(self, size): Initializes a Square object with a given size.

    """

    def __init__(self, size = 0):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square.

        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is a negative integer.

        """
        if value.isdigit():
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("Size must be >= 0")
        else:
            raise TypeError("Size must be an integer")