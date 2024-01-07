"""
Module: type_comparison

This module provides a function to check if an object belongs to a specified class or any of its subclasses.

Functions:
- is_kind_of_class(obj, a_class): Check if an object belongs to a specified class or any of its subclasses.

"""

def is_kind_of_class(obj, a_class):
    """
    Check if an object belongs to a specified class or any of its subclasses.

    Parameters:
    - obj: An object to be checked.
    - a_class: A class to compare the object's type with.

    Returns:
    - True if the object is an instance of the specified class or any of its subclasses.
    - False otherwise.
    """
    return isinstance(obj, a_class)