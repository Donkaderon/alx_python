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
        """
        Displays the rectangle by printing a representation of its shape using '#' symbols.

        The display is achieved by iterating over the height and width of the rectangle and printing '#' symbols.
        Each '#' symbol represents a pixel of the rectangle. The width represents the number of pixels in a row,
        and the height represents the number of rows. The '#' symbols are printed row by row, with each row
        separated by a newline character.

        The method also takes into account the x and y coordinates of the rectangle's position. It prints empty lines
        before the rectangle's top-left corner based on the value of x, and it prints '$' symbols before the rectangle's
        left side based on the value of y.

        For example, a rectangle with width 3, height 2, x 2, and y 1 would be displayed as:
        $##
        $##
        """
        for _ in range(self.__y):
            print('')

        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end='')
            for _ in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        The string representation includes information about the rectangle's id, width, height, x-coordinate, and y-coordinate.

        Returns:
         - A string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
    Updates the attributes of the object with the provided values.

    The `update` method accepts a variable number of arguments (`*args`), which can be used to update
    the attributes of the object. The arguments should be provided in the order corresponding to the
    attributes that need to be updated.

    Parameters:
        *args: Variable number of arguments representing the values to update the object's attributes.

    Usage:
        # Create an object
        obj = MyClass()

        # Update attributes using the update method
        obj.update(arg1, arg2, ...)

    Example:
        # Create a rectangle object
        rectangle = Rectangle(5, 3)

        # Update the rectangle's attributes using the update method
        rectangle.update(8, 6)

        # Now the rectangle's width is 8 and height is 6
    """
        if args:
            self.id = args[0]

            if len(args) >= 2:
                self.__width = args[1]

            if len(args) >= 3:
                self.__height = args[2]

            if len(args) >= 4:
                self.__x = args[3]

            if len(args) >= 5:
                self.__y = args[4]
        
        for key, value in kwargs.items():
            if key == 'id' in kwargs:
                self.id = value
            if key =='width' in kwargs:
                self.__width = value
            if key == 'height' in kwargs:
                self.__height = value
            if key =='x' in kwargs:
                self.__x = value
            if key =='y' in kwargs:
                self.__y = value






r = Rectangle(10, 12)
if r.y != 0:
    print("y must be equal to 0: {}".format(r.y))
    exit(1)

r.update(width=4)
    
if r.width != 4:
    print("width must be updated to 4: {}".format(r.width))
    exit(1)
    
if r.height != 12:
    print("height must stay to 12: {}".format(r.height))
    exit(1)

if r.x != 0:
    print("x must stay to 0: {}".format(r.x))
    exit(1)

if r.y != 0:
    print("y must stay to 0: {}".format(r.y))
    exit(1)
    
print("OK", end="")