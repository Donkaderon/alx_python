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
        __init__(self, size=0): Initializes a Square object with a given size.

    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square. Default is 0.

        """
        self.__size = size