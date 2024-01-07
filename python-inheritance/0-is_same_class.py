"""
Module: type_comparison

This module provides a function to compare the type of an object with a specified class.

Functions:
- is_same_class(obj, a_class): Check if an object belongs to a specified class.

"""
def is_same_class(obj, a_class):
    """
    Check if an object belongs to a specified class.

    Parameters:
    - obj: An object to be checked.
    - a_class: A class to compare the object's type with.

    Returns:
    - True if the object's type is the same as the specified class.
    - False otherwise.
    """
    return type(obj) == a_class

