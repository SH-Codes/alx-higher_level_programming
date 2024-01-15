#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self._validate_property(value, "width")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_property(value, "height")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self._validate_property(value, "x")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self._validate_property(value, "y")
        self.__y = value

    def _validate_property(self, value, property_name):
        """Validate and raise errors for property values."""
        if type(value) != int:
            raise TypeError(f"{property_name} must be an integer")
        if value < 0 and property_name in ["x", "y"]:
            raise ValueError(f"{property_name} must be >= 0")
        if value <= 0 and property_name in ["width", "height"]:
            raise ValueError(f"{property_name} must be > 0")

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle."""
        if args:
            self._update_with_args(args)
        elif kwargs:
            self._update_with_kwargs(kwargs)

    def _update_with_args(self, args):
        """Update the Rectangle with positional arguments."""
        attributes = ["id", "width", "height", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, attributes[i], value)

    def _update_with_kwargs(self, kwargs):
        """Update the Rectangle with keyword arguments."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

