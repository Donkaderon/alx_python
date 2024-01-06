"""
The square module provides a class to represent a square shape.

Module: square

Classes:
    Square: Represents a square shape.

"""

class Square:
    def __init__(self, size=0):
        """
        Square class represents a square shape.

        Args:
            size (int): The size of the square. Default is 0.

        Attributes:
            __size (int): Private instance attribute representing the size of the square.

        """
        self.__size = size
