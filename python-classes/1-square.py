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

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is a negative integer.

        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size