#!/usr/bin/python3
"""
class MyList Module
"""


class MyList(list):
    """this Class with method print_sorted"""
    pass

    def print_sorted(self):
        """thisMethot that sorted a list"""

        print(sorted(list(self)))
