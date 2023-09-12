#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
class BaseGeometry module
"""


class Square(Rectangle):
    """this class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """this method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """this is rectangle area"""

        return self.__size ** 2
