#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square."""
        if args:
            self._update_with_args(args)
        elif kwargs:
            self._update_with_kwargs(kwargs)

    def _update_with_args(self, args):
        """Update the Square with positional arguments."""
        attributes = ["id", "size", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, attributes[i], value)

    def _update_with_kwargs(self, kwargs):
        """Update the Square with keyword arguments."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

