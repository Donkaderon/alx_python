"""
Module: type_comparison

This module provides a function to check if an object inherits from a specified class.

Functions:
- inherits_from(obj, a_class): Check if an object inherits from a specified class.

"""

def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specified class.

    Parameters:
    - obj: An object to be checked.
    - a_class: A class to compare with the object's class hierarchy.

    Returns:
    - True if the object inherits from the specified class.
    - False otherwise.
    """
    return issubclass(type(obj), a_class)

a = 1
print(inherits_from(a, int))

a = [1, 2, 3]
print(inherits_from(a, list))