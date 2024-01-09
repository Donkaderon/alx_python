"""
The Base module provides a class for creating objects with unique identifiers.
"""
class Base: 
    """
    The Base class represents a blueprint for creating objects with unique identifiers.
    """

    __nb_objects = 0
    """
    Private class variable that keeps track of the number of objects created from the Base class.
    """

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        
        Parameters:
         - id (optional): An integer representing the unique identifier for the object.
        
        If id is not provided, the object is assigned a unique identifier based on the number of objects created.
        """
        if id is None: 
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else: 
            self.id = id