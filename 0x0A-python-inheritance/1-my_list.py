#!/usr/bin/python3
'''this Module for MyList class.'''


class MyList(list):
    '''Custom MyList class.'''
    def print_sorted(self):
        '''Method for printing sorted list.'''
        print(sorted(self))
