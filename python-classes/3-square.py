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
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is a negative integer.

        Notes:
            The size attribute is a private attribute prefixed with double underscores (__).

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and prints the area of the square.

        """
        self.area = self.__size * self.__size
        return self.area
    

