"""
This module defines the Square class, which is a special type of rectangle.

Classes:
    Square: Represents a square shape.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, which inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): The size (width and height) of the square.
            x (int, optional): The x-coordinate of the square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the square's position. Defaults to 0.
            id (int, optional): The ID of the square. Defaults to None.

        Note:
            The width and height of the square will be set to the value of `size`.

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get or set the size (width and height) of the square.

        Returns:
            int: The size (width and height) of the square.

        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size (width and height) of the square.

        Args:
            value (int): The new size (width and height) of the square.

        Raises:
            ValueError: If the provided value is not a positive integer.

        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Size must be a positive integer.")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The string representation of the square.

        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)