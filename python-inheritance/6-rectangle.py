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
    
    def area(self):
        """

        Calculate the area of the geometry.

        This method is intended to be overridden by subclasses to provide
        the specific implementation for calculating the area of the geometry.

        Raises:
        - Exception: Indicates that the 'area' method is not implemented.

        Returns:
        - None
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        self.__value = value
        self.__name = name
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        super().__init__()

        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
