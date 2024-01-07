"""
Module: geometry

This module provides a base class for geometry-related operations.

Classes:
- BaseGeometry: A base class for geometry operations.
"""

class BaseGeometry:
    """
    A base class for geometry operations.

    This class serves as a base for implementing specific geometry-related operations.
    It does not provide any specific functionality and is intended to be subclassed.

    Methods:
    - None
    """

    def integer_validator(self, name, value):
        self.__value = value
        self.__name = name
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    This class inherits from the BaseGeometry class and provides functionality
    to create and work with rectangles.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.

    Methods:
    - __init__(width, height): Initializes a new instance of the Rectangle class.
    - area(): Calculates the area of the rectangle.
    - __str__(): Returns a string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

        Raises:
        - TypeError: If either the width or height is not an integer.
        - ValueError: If either the width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height

        super().__init__()

        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        - int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        - str: A string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"