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


"""
The rectangle module provides the Rectangle class, which represents a rectangle object with getters and setters for its attributes.
"""
class Rectangle(Base):
    """
    The Rectangle class represents a rectangle object that inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
         - width: The width of the rectangle.
         - height: The height of the rectangle.
         - x (optional): The x-coordinate of the rectangle's position.
         - y (optional): The y-coordinate of the rectangle's position.
         - id (optional): An integer representing the unique identifier for the rectangle.

        If id is not provided, the rectangle is assigned a unique identifier based on the number of objects created.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Returns the width of the rectangle.
        """


    @width.setter
    def width(self, width):
        """
        Sets the width of the rectangle.

        Parameters:
         - width: The new width value for the rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Returns the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height of the rectangle.

        Parameters:
         - height: The new height value for the rectangle.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Returns the x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets the x-coordinate of the rectangle's position.

        Parameters:
         - x: The new x-coordinate value for the rectangle's position.
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Returns the y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Sets the y-coordinate of the rectangle's position.

        Parameters:
         - y: The new y-coordinate value for the rectangle's position.
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
         - The area value of the rectangle instance.
        """
        return self.__height * self.__width
    
    def display(self):
        for _ in range(self.__height):
            for _ in range(self.__width):
                print('#', end='')
            print()

