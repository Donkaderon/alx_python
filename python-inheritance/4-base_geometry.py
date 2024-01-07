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
        if self.area == 0 or self.area is None:
            raise NotImplementedError("area() is not implemented")

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))