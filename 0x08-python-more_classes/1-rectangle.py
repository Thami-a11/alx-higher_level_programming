#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
      """ init Rectange.
      
      Args:
      Width: the width of the new Triangle.
      height: The height of the new Triangle."""

      self.width = width
      self.height = height

@property
def width(self):
   """Get/set the width of the rectangle."""
  return self.__width

@width.setter
def width(self, value):
  if not isinstance(value, int):
    raise TypeError("Value must be interger.")
  if value < 0:
    raise TypeError("Value should be not be less than 0")
  return self.__height

@property
def height(self):
  """Get/set the Height of the rectangle."""
  return self.__height

@hight.setter
def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be interger.")
        if value < 0:
            raise ValueError("Value should be not be less than 0")
        self.__height = value
