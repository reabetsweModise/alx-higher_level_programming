#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module with class BaseGeometry
"""


class Square(Rectangle):
    """ this class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """this method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
